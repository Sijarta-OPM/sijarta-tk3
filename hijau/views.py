from django.shortcuts import render, redirect
from django.db import connection
# Create your views here.

def view_subkategori_jasa(request, id):
    context = {
        'logged_in' : True,
        'is_pelanggan': True,
    }
    
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
            return redirect('home:login')

        context['user'] = user

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

    with connection.cursor() as cursor:   
        cursor.execute(
            '''
            select * from public.subkategori_jasa
            where id = %s
            ''', [id]
        )
        subkategori_jasa = cursor.fetchone()
        context['subkategori_jasa'] = subkategori_jasa

    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.kategori_jasa
            where id = %s
            ''', [subkategori_jasa[3]]
        )
        kategori_jasa = cursor.fetchone()
        context['kategori_jasa'] = kategori_jasa
    
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.sesi_layanan
            where subkategoriid = %s
            ''', [id]
        )
        context['sesi_layanan'] = cursor.fetchall()
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
    return render(request, 'subkategori.html', context)
