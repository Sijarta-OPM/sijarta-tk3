from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.core import serializers
import json
from django.http import JsonResponse
from django.db import connection, DatabaseError
import uuid

def create_session(request, userId):
    sessionId = uuid.uuid4()
    with connection.cursor() as cursor:
        cursor.execute("""
            insert into session (sessionId, userId)
            values (%s, %s)
        """,[sessionId, userId])
    request.session['sessionId'] = str(sessionId)

def register(request):
    if (request.method == 'POST'):
        id = uuid.uuid4()
        data = json.loads(request.body)
        nama = data.get('nama')
        jeniskelamin = data.get('jeniskelamin')
        nohp = data.get('nohp')
        print(nohp)
        pwd = data.get('pwd')
        tgllahir = data.get('tgllahir')
        alamat = data.get('alamat')
        is_pelanggan = data.get('is_pelanggan')
        print(is_pelanggan)
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    insert into public.user (
                    id, nama, jeniskelamin, nohp, pwd, tgllahir, alamat, saldomypay
                    )
                    values 
                    (%s, %s, %s, %s, %s, %s, %s, 0)
                    ''', [id, nama, jeniskelamin, nohp, pwd, tgllahir, alamat]
                )
                if (is_pelanggan == 'true'):
                    cursor.execute(
                        '''
                        insert into public.pelanggan (id, level)
                        values (%s, 'Basic')
                        ''', [id]
                    )
                else :
                    namabank = data.get('namabank')
                    print(namabank)
                    nomorrekening = data.get('nomorrekening')
                    print(nomorrekening)
                    npwp = data.get('npwp')
                    print(npwp)
                    linkfoto = data.get('linkfoto')
                    print(linkfoto)
                    with connection.cursor() as cursor:
                        print("HELLO")
                        cursor.execute( 
                            '''
                            insert into public.pekerja
                            values (%s, %s, %s, %s, %s, 0, 0)
                            ''', [id, namabank, nomorrekening, npwp, linkfoto]
                        )
                        cursor.execute(
                            '''
                            select * from public.pekerja where id = %s
                            ''', [id]
                        )
                        print(cursor.fetchone())
            created = True
        except DatabaseError:
            created = False
        return JsonResponse({
            'status' : 'success',
            'created' : created
        })        
    return render(request, 'register.html')

def login(request):
    if (request.method == 'POST'):
        noHp = request.POST.get('noHp')
        password = request.POST.get('password')

        # buat query untuk mencari noHp dan password
        with connection.cursor() as cursor:
            cursor.execute("""
            select * from public.user u where u.pwd = %s and u.nohp = %s
            """, [password, noHp])
            
            user = cursor.fetchone()

            if (not user):
                messages.error(request, 'No HP atau password salah')
            else:
                create_session(request, user[0])
                messages.success(request, 'Kamu berhasil login')
                return redirect('home')
        
    return render(request, 'login.html')

def logout(request):
    if (request.session['sessionId'] != ''):
        connection.cursor().execute(
            """
            delete from 
                public.session s 
            where 
                s.sessionId = %s
            """, [request.session['sessionId']])
    return redirect('home')

def show_homepage(request):

    if 'sessionId' in request.session:
        sessionId=  request.session['sessionId']
        if (sessionId != ''):
            with connection.cursor() as cursor:
                cursor.execute("""
                    select * from public.user u
                    join public.session s
                    on u.id = s.userid
                    where s.sessionid = %s
                """, [sessionId])
                user = cursor.fetchone()

                if (user):
                    cursor.execute("""
                        select * from public.pelanggan
                        where id = %s
                    """, [str(user[0])])
                    pelanggan = cursor.fetchone()

                    if (pelanggan):
                        context = {
                            'logged_in' : True,
                            'role' : pelanggan,
                            'user' : user,
                            'is_pelanggan': True,
                        }
                    else:
                        cursor.execute("""
                            select * from public.pekerja
                            where id = %s
                        """, [str(user[0])])
                        pekerja = cursor.fetchone()
                        context = {
                            'logged_in' : True,
                            'role' : pekerja,
                            'user' : user,
                            'is_pelanggan': False,
                        }
                    print("successfully create session")

                    # load kategori jasa and subkategori
                    cursor.execute(
                        """
                        select * 
                        from public.kategori_jasa
                        """
                    )
                    kategori_jasa = cursor.fetchall()
                    print(kategori_jasa)
                    subkategori_by_kategori = {}
                    for kategori in kategori_jasa:
                        cursor.execute("""
                            select * from public.subkategori_jasa
                            where kategorijasaid = %s
                        """, [kategori[0]])
                        subkategori_jasa = cursor.fetchall()
                        subkategori_by_kategori[kategori[0]] = subkategori_jasa

                    context['kategori_jasa'] = kategori_jasa

                    context['subkategori_jasa'] = subkategori_by_kategori

                    return render(request, 'homepage.html', context)
                                    
                
    print("no session was found, please log in!")

    context = {
        'logged_in' : False,
        'is_pelanggan': False,
    }
    return render(request, 'homepage.html', context)

def show_profile(request, id):
    # get user by id
    context = {}
    with connection.cursor() as cursor:
        # check who access this page
        cursor.execute (
            '''
            select 
                * 
            from 
                public.user
            where 
                id in (
                    select 
                        userid 
                    from 
                        public.session
                    where 
                        sessionid = %s
            )''', [request.session['sessionId']]
        )

        user_who_access = cursor.fetchone()

        cursor.execute(
            '''
            select 
                * 
            from 
                public.pelanggan 
            where 
                id = %s    
            ''', [user_who_access[0]]
        )
        if cursor.fetchone():
            user_who_access_is_pelanggan = True
        else :
            user_who_access_is_pelanggan = False
        
        cursor.execute("""
            select * from public.user where id = %s
        """, [id])
        user = cursor.fetchone()
        
        # find whether it is pelanggan or pekerja
        cursor.execute("""
            select * from public.pekerja where id = %s
        """, [id])
        pekerja = cursor.fetchone()
        if (pekerja):
            role = pekerja
            is_pelanggan = False
        else:
            cursor.execute("""
            select * from public.pelanggan where id = %s
            """, [id])
            is_pelanggan = True
            role = cursor.fetchone()

        cursor.execute(
            '''
            select my.nominal, my.tgl, tm.nama 
            from public.kategori_tr_mypay tm
            join public.tr_mypay my
            on tm.id = my.kategoriid
            where my.userid = %s
            ''', [user[0]]
        )
        transaksi = cursor.fetchall()
        if (user != user_who_access):
            temp = user
            user = user_who_access
            user_who_access = temp
        
        
    context = {
        'user':user,
        'role': role,
        'user_who_access_is_pelanggan' : user_who_access_is_pelanggan,
        'is_pelanggan':is_pelanggan,
        'logged_in':True,
        'user_who_access': user_who_access,
        'list_transaksi' : transaksi
        
    }
    return render(request, 'profile.html', context)

def show_kategori_by_id(request, id):
    with connection.cursor() as cursor:
        cursor.execute('''
            select distinct id, deskripsi from public.subkategori
            where kategorijasaid = %s
        ''', [id])
        subkategori = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        subkategori_list = [
            dict(zip(columns, row))
            for row in subkategori
        ]
        return JsonResponse({
            'status': 'success',
            'data': subkategori_list,
        }, safe=False)

def search_subkategori(request):
    data = json.loads(request.body)

    kategori_jasa = data.get('kategoriJasa', '')
    subkategori_jasa = data.get('subkategoriJasa', '').strip()
    
    subkategori_jasa = f"%{subkategori_jasa}%"
    with connection.cursor() as cursor:
        if (not kategori_jasa):
            if (not subkategori_jasa):
                cursor.execute(
                    '''
                    select 
                        kj.id idkategori, 
                        kj.namakategori namakategori,
                        skj.id idsubkategori,
                        skj.namasubkategori namasubkategori
                    from 
                        public.kategori_jasa kj
                    join
                        public.subkategori_jasa skj
                    on 
                        kj.id = skj.kategorijasaid
                    
                    ''', 
                )
            else:
                cursor.execute(
                    '''
                    select 
                        kj.id idkategori, 
                        kj.namakategori namakategori,
                        skj.id idsubkategori,
                        skj.namasubkategori namasubkategori
                    from 
                        public.kategori_jasa kj
                    join
                        public.subkategori_jasa skj
                    on 
                        kj.id = skj.kategorijasaid
                    where
                        namasubkategori ilike %s
                    ''', [subkategori_jasa]
                )
        else:
            cursor.execute(
                '''
                select 
                    kj.id idkategori, 
                    kj.namakategori namakategori,
                    skj.id idsubkategori,
                    skj.namasubkategori namasubkategori
                from 
                    public.kategori_jasa kj
                join
                    public.subkategori_jasa skj
                on 
                    kj.id = skj.kategorijasaid
                where
                    kj.namakategori like %s 
                    and skj.namasubkategori ilike %s
                
                ''', [kategori_jasa, subkategori_jasa]
            )

        subkategori_jasa = dict()
        
        columns = [col[0] for col in cursor.description]
        for subkategori in cursor.fetchall():
            key = str(subkategori[0])
            value = {}
            for i in range(1,4):
                value[str(columns[i])] = str(subkategori[i])
            if key in subkategori_jasa:
                try:
                    subkategori_jasa[key] += [value]
                except:
                    print("not list appearantly")
            else:
                subkategori_jasa[key] = [(value)]
        return JsonResponse({
            'status': 'success',
            'data' : subkategori_jasa,
        }, safe=False
        )

        
def show_subkategori_by_id(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            select id, namasubkategori, kategorijasaid 
            from public.subkategori_jasa 
            where kategorijasaid = %s
        """, [id])
        
        columns = [col[0] for col in cursor.description]
        subkategori_list = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        
        return JsonResponse({
            'status': 'success',
            'data': subkategori_list
        }, safe=False)

def view_pemesanan_jasa(request):
    if 'sessionId' in request.session:
        sessionId =  request.session['sessionId']
        if (sessionId != ''):
            with connection.cursor() as cursor:
                cursor.execute("""
                    select * from public.user u
                    join public.session s
                    on u.id = s.userid
                    where s.sessionid = %s
                """, [sessionId])
                user = cursor.fetchone()

                if (user):
                    cursor.execute("""
                        select * from public.pelanggan
                        where id = %s
                    """, [str(user[0])])
                    pelanggan = cursor.fetchone()

                    if (pelanggan):
                        context = {
                            'logged_in' : True,
                            'role' : pelanggan,
                            'user' : user,
                            'is_pelanggan': True,
                        }
                    else:
                        cursor.execute("""
                            select * from public.pekerja
                            where id = %s
                        """, [str(user[0])])
                        pekerja = cursor.fetchone()
                        context = {
                            'logged_in' : True,
                            'role' : pekerja,
                            'user' : user,
                            'is_pelanggan': False,
                        }
                    print("successfully access")

                    # load pekerjaan yang sudah dibayar oleh user, tetapi belom dikarjakan pekerja lain
                    cursor.execute(
                        '''
                        select
                            pj.id idpemesanan, 
                            kj.id idkategori, 
                            kj.namakategori,
                            skj.id idsubkategori,
                            skj.namasubkategori
                        from 
                            public.tr_pemesanan_status ps
                        join
                            public.tr_pemesanan_jasa pj
                        on
                            pj.id = ps.idtrpemesanan
                        join
                            public.subkategori_jasa skj
                        on 
                            skj.id = pj.idkategorijasa
                        join
                            public.kategori_jasa kj
                        on 
                            kj.id = skj.kategorijasaid
                        join
                            public.pekerja_kategori_jasa kkj
                        on 
                            kkj.kategorijasaid = kj.id
                        where 
                            ps.idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                            and kkj.pekerjaid = %s
                        ''',[user[0]]
                    )
                    pekerjaan_tersedia = cursor.fetchall()
                    context['pekerjaan_tersedia'] = pekerjaan_tersedia
                    print(pekerjaan_tersedia)
                    # extract kategori pekerjaan
                    kategori_jasa = []
                    for pekerjaan in pekerjaan_tersedia:
                        if [pekerjaan[1], pekerjaan[2]] not in kategori_jasa:
                            kategori_jasa.append([pekerjaan[1], pekerjaan[2]])

                    context['kategori_jasa'] = kategori_jasa
                    return render(request, 'pekerjaan_jasa.html', context)
                                    
                
    print("no session was found, please log in!")
    return redirect('login')

def view_status_pemesanan_jasa(request):
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('login')
    role = get_pekerja(user[0])
    is_pelanggan = False
    if (not role):
        is_pelanggan = True
        role = get_pelanggan(user[0])
    # user and its role already defined, next 
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select 
                kj.id,
                kj.namakategori
            from 
                public.kategori_jasa kj
            join
                public.pekerja_kategori_jasa pkj
            on
                pkj.kategorijasaid = kj.id
                and pkj.pekerjaid = %s
            ''', [user[0]]
        )
        kategori = cursor.fetchall()

        cursor.execute(
            '''
            select * from public.status_pesanan
            where id not in ('3fa85f64-5717-4562-b3fc-2c963f66afa6', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9')
            '''
        )
        status = cursor.fetchall()
        
    context = {
        'user': user,
        'role': role,
        'is_pelanggan' : is_pelanggan,
        'logged_in' : True,
        'kategori_pemesanan' : kategori,
        'status_pesanan' : status

    }
    
    return render(request, 'status_pekerjaan_jasa.html', context)

def get_pemesanan(request):
    user = get_user(request.session['sessionId'])
    if not user:
        return redirect('login')
    # data = json.loads(request.body)
    kategori = request.GET.get('kategorijasa', '').strip()
    subkategori = request.GET.get('subkategorijasa', '').strip()
    with connection.cursor() as cursor:
        if (kategori == ""):
            cursor.execute(
                '''
                select
                    skj.namasubkategori,
                    pelanggan.nama namapelanggan,
                    pj.tglpemesanan,
                    pj.tglpekerjaan,
                    pj.totalbiaya,
                    ps.idtrpemesanan           

                from 
                    public.tr_pemesanan_status ps
                join
                    public.tr_pemesanan_jasa pj
                on
                    pj.id = ps.idtrpemesanan
                join
                    public.subkategori_jasa skj
                on 
                    skj.id = pj.idkategorijasa
                join
                    public.kategori_jasa kj
                on 
                    kj.id = skj.kategorijasaid
                join 
                    public.user pelanggan
                on 
                    pelanggan.id = pj.idpelanggan
                join 
                    public.pekerja_kategori_jasa pkj
                on
                    pkj.kategorijasaid = kj.id
                where 
                    ps.idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                    and pkj.pekerjaid = %s
                ''', [user[0]]
            )
            result = cursor.fetchall()
        else:
            cursor.execute(
                '''
                select
                    skj.namasubkategori,
                    pelanggan.nama namapelanggan,
                    pj.tglpemesanan,
                    pj.tglpekerjaan,
                    pj.totalbiaya,
                    ps.idtrpemesanan           
                from 
                    public.tr_pemesanan_status ps
                join
                    public.tr_pemesanan_jasa pj
                on
                    pj.id = ps.idtrpemesanan
                join
                    public.subkategori_jasa skj
                on 
                    skj.id = pj.idkategorijasa
                join
                    public.kategori_jasa kj
                on 
                    kj.id = skj.kategorijasaid
                join 
                    public.user pelanggan
                on 
                    pelanggan.id = pj.idpelanggan
                join 
                    public.pekerja_kategori_jasa pkj
                on
                    pkj.kategorijasaid = kj.id
                where 
                    ps.idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                    and kj.id = %s
                    and pkj.pekerjaid = %s
                ''',[kategori, user[0]]
            )
            if (subkategori):
                cursor.execute(
                '''
                select
                    skj.namasubkategori,
                    pelanggan.nama namapelanggan,
                    pj.tglpemesanan,
                    pj.tglpekerjaan,
                    pj.totalbiaya,
                    ps.idtrpemesanan           

                from 
                    public.tr_pemesanan_status ps
                join
                    public.tr_pemesanan_jasa pj
                on
                    pj.id = ps.idtrpemesanan
                join
                    public.subkategori_jasa skj
                on 
                    skj.id = pj.idkategorijasa
                join
                    public.kategori_jasa kj
                on 
                    kj.id = skj.kategorijasaid
                join 
                    public.user pelanggan
                on 
                    pelanggan.id = pj.idpelanggan
                join 
                    public.pekerja_kategori_jasa pkj
                on
                    pkj.kategorijasaid = kj.id
                where 
                    ps.idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                    and kj.id = %s
                    and skj.id = %s
                    and pkj.pekerjaid = %s
                ''',[kategori, subkategori, user[0]]
            )
            result = cursor.fetchall()
        print(result)
        return JsonResponse({
            'status' : 'success',
            'data' : result
        }, safe=False)

def get_subkategori_pemesanan(request):
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('login')
    idkategorijasa = request.GET.get('idKategoriJasa','').strip()

    
    with connection.cursor() as cursor:
        if (idkategorijasa):
            cursor.execute(
                '''
                select
                    distinct
                    skj.id idsubkategori,
                    skj.namasubkategori
                from 
                    public.tr_pemesanan_status ps
                join
                    public.tr_pemesanan_jasa pj
                on
                    pj.id = ps.idtrpemesanan
                join
                    public.subkategori_jasa skj
                on 
                    skj.id = pj.idkategorijasa
                join
                    public.kategori_jasa kj
                on 
                    kj.id = skj.kategorijasaid
                where 
                    ps.idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                    and kj.id = %s
                ''', [idkategorijasa]
            )
            subkategori = cursor.fetchall()
            return JsonResponse({
                'status' : 'success',
                'data' : subkategori
            }, safe=False)
        else:
            return JsonResponse({
                'status' : 'success'
            })


def get_user(sessionId):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select 
                *
            from 
                public.user u,
                public.session s
            where
                u.id = s.userid
                and s.sessionId = %s
            ''', [sessionId]
        )
        user = cursor.fetchone()
        if (user):
            return user
        else:
            return

def is_pelanggan(userid):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select
                *
            from
                public.pelanggan
            where id = %s
            ''', [userid]
        )
        if (cursor.fetchone()):
            return True
        else :
            return False
def get_pelanggan(userid):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select
                *
            from
                public.pelanggan
            where id = %s
            ''', [userid]
        )
        return cursor.fetchone()
def get_pekerja(userid):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select
                *
            from
                public.pekerja
            where id = %s
            ''', [userid]
        )
        return cursor.fetchone()

def kerjakan_pemesesanan_jasa(request):
    '''
    kerjakan_pemesanan_jasa adalah api yang digunakan untuk update status pemesanan 
    pelanggan dari pembayaran dikonfirmasi
    menjadi pekerja sedang menuju ke lokasi
    '''
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('login')
    data = json.loads(request.body)
    idtrpemesanan = data.get('idtrpemesanan', '').strip()
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            update public.tr_pemesanan_status
            set
                idstatus = 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8'
            where
                idtrpemesanan = %s
                and idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
            ''', [idtrpemesanan]
        )
        cursor.execute(
            '''
            update public.tr_pemesanan_jasa
            set 
                idpekerja = %s,
                tglpekerjaan = NOW()
            where 
                id = %s
            ''', [user[0], idtrpemesanan]
        )
    return JsonResponse({
        'status' : 'success' 
    })

def get_status_pemesanan(request):
    pekerja = get_user(request.session['sessionId'])
    data = json.loads(request.body)
    kategori_jasa =  data.get('kategori')
    status_pesanan =  data.get('status')
    with connection.cursor() as cursor:
        if (not kategori_jasa):
            if (not status_pesanan):
                    cursor.execute(
                        '''
                        select 
                            skj.namasubkategori nama_subkategori_pesanan,
                            pj.tglpemesanan tanggal_pemesanan,
                            pelanggan.nama nama_pelanggan,
                            pj.tglpekerjaan tanggal_pekerjaan,
                            pj.totalbiaya total_biaya,
                            sp.status status_pesanan,
                        ps.idtrpemesanan
                        from 
                            public.tr_pemesanan_status ps
                        join   
                            public.tr_pemesanan_jasa pj
                        on
                            pj.id = ps.idtrpemesanan
                        join 
                            public.subkategori_jasa skj
                        on
                            skj.id = pj.idkategorijasa
                        join 
                            public.user pelanggan
                        on
                            pelanggan.id = pj.idpelanggan
                        join
                            public.status_pesanan sp
                        on
                            sp.id = ps.idstatus
                        where 
                            ps.idstatus not in 
                            ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 
                            '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', 
                            'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9')
                            and pj.idpekerja = %s
                        ''', [pekerja[0]]
                    )
                    result = cursor.fetchall()
            else:
                cursor.execute(
                    '''
                    select 
                        skj.namasubkategori nama_subkategori_pesanan,
                        pj.tglpemesanan tanggal_pemesanan,
                        pelanggan.nama nama_pelanggan,
                        pj.tglpekerjaan tanggal_pekerjaan,
                        pj.totalbiaya total_biaya,
                        sp.status status_pesanan,
                        ps.idtrpemesanan
                    from 
                        public.tr_pemesanan_status ps
                    join   
                        public.tr_pemesanan_jasa pj
                    on
                        pj.id = ps.idtrpemesanan
                    join 
                        public.subkategori_jasa skj
                    on
                        skj.id = pj.idkategorijasa
                    join 
                        public.user pelanggan
                    on
                        pelanggan.id = pj.idpelanggan
                    join
                        public.status_pesanan sp
                    on
                        sp.id = ps.idstatus
                    where
                        ps.idstatus = %s
                        and pj.idpekerja = %s
                    ''',[status_pesanan, pekerja[0]]
                )
                result = cursor.fetchall()
        else:
            if (status_pesanan):
                cursor.execute(
                    '''
                    select 
                        skj.namasubkategori nama_subkategori_pesanan,
                        pj.tglpemesanan tanggal_pemesanan,
                        pelanggan.nama nama_pelanggan,
                        pj.tglpekerjaan tanggal_pekerjaan,
                        pj.totalbiaya total_biaya,
                        sp.status status_pesanan,
                        ps.idtrpemesanan
                    from 
                        public.tr_pemesanan_status ps
                    join
                        public.status_pesanan sp
                    on
                        sp.id = ps.idstatus
                    join   
                        public.tr_pemesanan_jasa pj
                    on
                        pj.id = ps.idtrpemesanan
                    join 
                        public.subkategori_jasa skj
                    on
                        skj.id = pj.idkategorijasa
                    join 
                        public.user pelanggan
                    on
                        pelanggan.id = pj.idpelanggan
                    join public.kategori_jasa kj
                    on
                        kj.id = skj.kategorijasaid
                    where
                        ps.idstatus = %s
                        and kj.id = %s
                        and pj.idpekerja = %s
                    ''', [status_pesanan, kategori_jasa, pekerja[0]]
                )
                result = cursor.fetchall()
            else:
                cursor.execute(
                    '''
                    select 
                        skj.namasubkategori nama_subkategori_pesanan,
                        pj.tglpemesanan tanggal_pemesanan,
                        pelanggan.nama nama_pelanggan,
                        pj.tglpekerjaan tanggal_pekerjaan,
                        pj.totalbiaya total_biaya,
                        sp.status status_pesanan,
                        ps.idtrpemesanan
                    from 
                        public.tr_pemesanan_status ps
                    join
                        public.status_pesanan sp
                    on
                        sp.id = ps.idstatus
                    join   
                        public.tr_pemesanan_jasa pj
                    on
                        pj.id = ps.idtrpemesanan
                    join 
                        public.subkategori_jasa skj
                    on
                        skj.id = pj.idkategorijasa
                    join 
                        public.user pelanggan
                    on
                        pelanggan.id = pj.idpelanggan
                    join public.kategori_jasa kj
                    on
                        kj.id = skj.kategorijasaid
                    where
                        kj.id = %s
                        and ps.idstatus not in 
                        (
                        '3fa85f64-5717-4562-b3fc-2c963f66afa6', 
                        '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', 
                        'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                        )
                        and pj.idpekerja = %s
                    ''', [kategori_jasa, pekerja[0]]
                )
                result = cursor.fetchall()
    return JsonResponse({
        'status' : 'success',
        'data' : result
    })

def update_status_pemesanan(request):
    user = get_user(request.session['sessionId'])
    if ( not user ):
        return redirect('login')
    # since user is logged in
    data = json.loads(request.body)
    idtrpemesanan = data.get('idtrpemesanan')
    connection.cursor().execute(
        '''
        select public.update_status(%s);
        ''', [idtrpemesanan]
    )
    
    return JsonResponse({
        'status' : 'success'
    })