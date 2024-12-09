from django.shortcuts import render, redirect
from django.db import connection, IntegrityError, DatabaseError
from main.views import get_user, get_pekerja, get_pelanggan
from django.http import JsonResponse
import uuid
import json
# Create your views here.

def view_subkategori_jasa(request, id):
    # Initialize context with default values
    context = {
        'logged_in' : True,
        'is_pelanggan': True,
    }
    
    # Fetch user information based on session ID
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.user u
            where u.id in (
                select userid from public.session
                where sessionid = %s
            )
            ''', [request.session['sessionId']]
        )
        user = cursor.fetchone()

        if not user:
            print("please log in")
            return redirect('home')

        context['user'] = user

        # Check if the user is a pelanggan or pekerja
        cursor.execute(
        """
            select * from public.pelanggan
            where id = %s
        """, [str(user[0])])

        pelanggan = cursor.fetchone()

        if (pelanggan):
            context['role'] = pelanggan
            context['is_pelanggan'] = True
        else:
            cursor.execute("""
                select * from public.pekerja
                where id = %s
            """, [str(user[0])])
            pekerja = cursor.fetchone()
            context['role'] = pekerja
            context['is_pelanggan'] = False

    # Fetch subkategori_jasa details
    with connection.cursor() as cursor:   
        cursor.execute(
            '''
            select * from public.subkategori_jasa
            where id = %s
            ''', [id]
        )
        subkategori_jasa = cursor.fetchone()
        context['subkategori_jasa'] = subkategori_jasa

    # Fetch kategori_jasa details
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.kategori_jasa
            where id = %s
            ''', [subkategori_jasa[3]]
        )
        kategori_jasa = cursor.fetchone()
        context['kategori_jasa'] = kategori_jasa
    
    # Fetch sesi_layanan details
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.sesi_layanan
            where subkategoriid = %s
            ''', [id]
        )
        context['sesi_layanan'] = cursor.fetchall()
    
    # Fetch pekerja details
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.user u join public.pekerja p
            on u.id = p.id
            where u.id in
            (
                select pekerjaid from public.pekerja_kategori_jasa
                where KategoriJasaId = %s
            )
            ''', [kategori_jasa[0]]
        )

        context['pekerja'] = cursor.fetchall()
    
    # Fetch testimoni details
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select 
                up.nama as pelanggan, 
                t.teks, 
                t.tgl, 
                uw.nama as pekerja, 
                t.rating

            from 
                public.testimoni t

            join 
                public.tr_pemesanan_jasa p
            on 
                t.idtrpemesanan = p.id

            join 
                public.user uw
            on 
                uw.id = p.idpekerja

            join 
                public.pekerja pk
            on 
                pk.id = uw.id

            join 
                public.user up
            on 
                up.id = p.idpelanggan

            join
                public.pelanggan pl
            on 
                pl.id = up.id

            where 
                idkategorijasa = %s
            ''', [id]
        )
        testimoni = cursor.fetchall()
        
        context['testimoni'] = testimoni
    
    # Render the subkategori.html template with the context
    return render(request, 'subkategori.html', context)

def check_diskon(request):
    # Load request data
    data = json.loads(request.body)
    potongan_harga = 0
    nominal = float(data.get('nominal').strip())
    kodediskon = data.get('kodediskon')
    user = get_user(request.session['sessionId'])
    
    # Check if the discount code is valid and applicable
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.diskon
            where kode = %s and mintrpemesanan < %s
            ''', [kodediskon, nominal]
        )
        diskon = cursor.fetchone()
        if (diskon):
            cursor.execute(
                '''
                select 
                    * 
                from 
                    public.promo p
                join
                    public.diskon d
                on
                    p.kode = d.kode
                where 
                    p.kode = %s
                    and tglakhirberlaku > CURRENT_DATE
                ''',[kodediskon]
            )
            tipe_diskon = cursor.fetchone()
            if (not tipe_diskon):
                cursor.execute(
                    '''
                    select 
                        * 
                    from 
                        public.tr_pembelian_voucher pv
                    join 
                        public.diskon d
                    on
                        d.kode = pv.idvoucher

                    where 
                        pv.idvoucher = %s
                        and idpelanggan = %s
                    ''', [kodediskon, user[0]]
                )
                tipe_diskon = cursor.fetchone()
                if (tipe_diskon):
                    # dipake = int(tipe_diskon[3]) + 1
                    try:
                        # cursor.execute(
                        #     '''
                        #     update
                        #         public.tr_pembelian_voucher
                        #     set
                        #         telahdigunakan = telahdigunakan + 1
                        #     where
                        #         idvoucher = %s and idpelanggan = %s
                        #     ''', [kodediskon, user[0]]
                        # )
                        potongan_harga = float(diskon[1]) /100 * nominal
                    except Exception as e:
                        print(e)
                        potongan_harga = 0
            else:
                potongan_harga = float(diskon[1])/100 * nominal       
    
    # Return the discount amount as JSON response
    return JsonResponse({
        'status' : 'success',
        'potongan_harga' : potongan_harga
    })

def add_pemesanan_jasa(request):
    # Get user information
    user = get_user(request.session['sessionId'])
    if not user:
        return redirect('home')
    
    # Ensure the user is a pelanggan
    pelanggan = get_pelanggan(user[0])
    if not pelanggan:
        return redirect('home')
    
    # Load request data
    data = json.loads(request.body)

    id = uuid.uuid4()
    tglpemesanan = data.get('tglpemesanan')
    totalbiaya = data.get('totalbiaya')
    idpelanggan = user[0]
    idkategorijasa = data.get('idkategorijasa')
    sesi = data.get('sesi')
    iddiskon = data.get('iddiskon')
    idmetodebayar = data.get('idmetodebayar')
    orderstatus = False
    if float(user[7]) < float(totalbiaya):
        orderstatus = False

    if idmetodebayar != 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb':
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                insert into public.tr_pemesanan_jasa
                (
                    id, tglpemesanan, totalbiaya,
                    idpelanggan, idkategorijasa, 
                    sesi, idmetodebayar
                )
                values
                (
                    %s, %s, %s,
                    %s, %s,
                    %s, %s
                )
                ''', [
                    id, tglpemesanan, totalbiaya,
                    idpelanggan, idkategorijasa,
                    sesi, idmetodebayar
                ]
            )
            cursor.execute(
                '''
                insert into public.tr_pemesanan_status
                values
                (%s, %s, %s)
                ''', [id, '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', tglpemesanan]
            )

    if float(user[7] >= float(totalbiaya)): # 
        orderstatus = True
        # Insert pemesanan_jasa record
        connection.cursor().execute(
            '''
            insert into public.tr_pemesanan_jasa
            (
                id, tglpemesanan, totalbiaya,
                idpelanggan, idkategorijasa, 
                sesi, idmetodebayar
            )
            values
            (
                %s, %s, %s,
                %s, %s,
                %s, %s
            )
            '''
            , [
                id, tglpemesanan, totalbiaya,
                idpelanggan, idkategorijasa,
                sesi, idmetodebayar
            ]
        )
        # Insert pemesanan_status record
        connection.cursor().execute(
            '''
            insert into public.tr_pemesanan_status
            values
            (%s, %s, %s)
            ''', [id, '3fa85f64-5717-4562-b3fc-2c963f66afa6', tglpemesanan]
        )
        # Update pemesanan_jasa with discount if applicable
        if (iddiskon):
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    update
                        public.tr_pembelian_voucher
                    set
                        telahdigunakan = telahdigunakan + 1
                    where
                        idvoucher = %s and idpelanggan = %s
                    ''', [iddiskon, user[0]]
                )
            connection.cursor().execute(
                '''
                update
                    public.tr_pemesanan_jasa
                set
                    iddiskon = %s
                where
                    id = %s
                ''', [iddiskon, id]
            )
    return JsonResponse({
        'status' : 'success',
        'orderstatus' : orderstatus
    })

def get_already_join(request):
    # Get user information
    user = get_user(request.session['sessionId'])
    is_registered = False
    if (not user):
        return redirect('home')

    # Check if the user is already registered as pekerja in any kategori_jasa
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT 
                *
            FROM 
                public.pekerja_kategori_jasa 
            WHERE
                pekerjaid = %s
            ''', [user[0]]
        )
        if (cursor.fetchone()):
            is_registered = True
    
    # Return the registration status as JSON response
    return JsonResponse({
        'status' : 'success',
        'is_registered' : is_registered
    })

def gabungkan_pekerja(request):
    # Get user information
    user = get_user(request.session['sessionId'])
    data = json.loads(request.body)

    kategori_jasa = data.get('kategorijasa')
    if (not user):
        return redirect('home')
    
    # Insert pekerja_kategori_jasa record
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                '''
                insert into public.pekerja_kategori_jasa
                values (%s, %s)
                ''', [user[0], kategori_jasa]
            )
        except DatabaseError:
            return JsonResponse({
                'status' : 'failed'
            })
    
    # Return success status as JSON response
    return JsonResponse({
        'status' : 'success'
    })