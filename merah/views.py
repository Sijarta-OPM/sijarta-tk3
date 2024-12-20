from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from datetime import date
from main.views import get_user
import uuid

# Function to handle top-up requests
def topup(request):
    nominal = int(request.POST.get('nominal').strip())
    with connection.cursor() as cursor:
        # Fetch user details based on session ID
        cursor.execute(
            '''
            select 
                * 
            from 
                public.user u, 
                public.session s
            where 
                u.id = s.userid and s.sessionid = %s
            ''', [request.session['sessionId']]
        )
        user = cursor.fetchone()
        # Update user's saldo
        cursor.execute(
            '''
            update 
                public.user
            set 
                saldomypay = %s
            where  
                id = %s;
            ''', [str(user[7]+nominal), user[0]]
        )
        # Insert transaction record
        cursor.execute(
            '''
            insert into public.tr_mypay(Id, UserId, Tgl, Nominal, KategoriId)
            values (%s, %s, %s, %s, %s)
            ''', [uuid.uuid4(), user[0], date.today(), nominal, 'cbf1aba9-2d20-45d6-844f-115cfabd252e']
        )
    return redirect('mypay:show_transaction_form')

# Function to handle payment requests
def payment(request):
    idpemesanan = request.POST.get('idpemesanan').strip()
    with connection.cursor() as cursor:
        # Fetch order and user details
        cursor.execute(
            '''
            select 
                pj.id idpemesanan, 
                pelanggan.id as idpelanggan, 
                pelanggan.saldomypay as saldopelanggan,
                pj.totalbiaya as total                
            from 
                public.tr_pemesanan_jasa pj
            join 
                public.user pelanggan 
            on
                pelanggan.id = pj.idpelanggan
            where pj.id = %s
            ''', [idpemesanan]
        )
        pemesanan_jasa = cursor.fetchone()
        # Check if user has sufficient saldo
        if float(pemesanan_jasa[2]) >= float(pemesanan_jasa[3]):
            cursor.execute(
                '''
                update 
                    public.user
                set 
                    saldomypay = %s
                where 
                    id = %s;

                insert into 
                    public.tr_mypay(Id, UserId, Tgl, Nominal, KategoriId)
                values 
                    (%s, %s, %s, %s, %s);

                update 
                    public.tr_pemesanan_status
                set 
                    idstatus = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9'
                where 
                    idtrpemesanan = %s;
                ''', [
                        str(pemesanan_jasa[2]-pemesanan_jasa[3]),
                        pemesanan_jasa[1],
                        uuid.uuid4(),
                        pemesanan_jasa[1],
                        date.today(),
                        str(-1*pemesanan_jasa[3]),
                        '41f85ca1-38dc-44fc-9283-25e2117f8d06',
                        pemesanan_jasa[0]
                    ]
            )
            
    return redirect('mypay:show_transaction_form')
        
# Function to get orders for the logged-in user
def get_order(request):
    user = get_user(request.session['sessionId'])

    with connection.cursor() as cursor:
        # Fetch orders for the user
        cursor.execute(
            '''
            select 
                pj.id idpemesanan, 
                pelanggan.id idpelanggan, 
                pelanggan.nama namapelanggan, 
                sj.namasubkategori namasubkategori, 
                sl.sesi sesi,
                pj.totalbiaya total, 
                sp.status 
            from 
                public.tr_pemesanan_status ps
            join 
                public.tr_pemesanan_jasa pj 
            on 
                ps.idtrpemesanan = pj.id
            join 
                public.status_pesanan sp 
            on 
                sp.id = ps.idstatus
            join 
                public.user pelanggan
            on 
                pelanggan.id = pj.idpelanggan
            join 
                public.sesi_layanan sl
            on 
                sl.subkategoriid = pj.idkategorijasa and sl.sesi = pj.sesi
            join 
                public.subkategori_jasa sj
            on 
                sj.id = sl.subkategoriid
            where 
                sp.id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' and pelanggan.id=%s 
            ''', [user[0]]
        )
        pesanan_jasa = cursor.fetchall()
        return JsonResponse(
            {
                'status': 'success',
                'data': pesanan_jasa
            }, safe=False
        )

# Function to handle transfer requests
def transfer(request):
    if (request.method == 'POST'):
        userid = request.POST.get('userid','').strip()
        noHp = request.POST.get('noHp', '').strip()
        nominal = int(request.POST.get('nominal'))

        with connection.cursor() as cursor:
            # Fetch sender details
            cursor.execute(
                '''
                select * from public.user asal
                where asal.id = %s
                ''', [userid]
            )
            pengirim = cursor.fetchone()
            if pengirim[7] < nominal:
                return redirect('mypay:show_transaction_form')
            
            # Fetch receiver details
            cursor.execute(
                '''
                select 
                    * 
                from 
                    public.user tujuan
                where 
                    tujuan.noHp like %s
                ''', [noHp]
            )
            
            penerima = cursor.fetchone()

            if (not penerima):
                return redirect('mypay:show_transaction_form')
            
            # Insert transaction records for both sender and receiver
            cursor.execute(
                    '''
                    insert into public.tr_mypay(Id, UserId, Tgl, Nominal, KategoriId)
                    values (%s, %s, %s, %s, %s)    
                    ''',[str(uuid.uuid4()), str(penerima[0]), str(date.today()), str(nominal), '8c7f9ffd-b369-470f-a59e-8bba08086923']
                )
            cursor.execute(
                    '''
                    insert into public.tr_mypay(Id, UserId, Tgl, Nominal, KategoriId)
                    values (%s, %s, %s, %s, %s)    
                    ''',[str(uuid.uuid4()), str(pengirim[0]), str(date.today()), str(-1*nominal), '8c7f9ffd-b369-470f-a59e-8bba08086923']
                )
            # Update saldo for both sender and receiver
            cursor.execute(
                '''
                update 
                    public.user
                set 
                    saldomypay = %s
                where 
                    id = %s
                ''', [str(penerima[7]+nominal), penerima[0]]
            )

            cursor.execute(
                '''
                update 
                    public.user
                set 
                    saldomypay = %s
                where 
                    id = %s
                ''', [str(pengirim[7]-nominal), pengirim[0]]
            )
    # Ensure the updates are successful
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select 
                *
            from 
                public.user
            where 
                id = %s or noHp= %s
            ''', [userid, noHp]
        )
    return redirect('mypay:show_transaction_form')
    
# Function to handle withdrawal requests
def withdraw(request):
    norek = request.POST.get('norek')
    nominal = request.POST.get('nominal')
    with connection.cursor() as cursor:
        # Fetch user details based on session ID and account number
        cursor.execute(
            '''
            select 
                * 
            from 
                public.user u, 
                public.pekerja p,
                public.session
            where 
                u.id = p.id
                and u.id = s.userid 
                and s.sessionid = %s
                and p.nomorrekening = '%s'
                
            ''', [request.session['sessionId'], norek]
        )
        user = cursor.fetchone()
        if (user):
            # Update user's saldo and insert transaction record
            cursor.execute(
                '''
                update
                    public.user
                set
                    saldomypay = %s
                where 
                    id = %s;
                
                insert into public.tr_mypay(Id, UserId, Tgl, Nominal, KategoriId)
                values (%s, %s, %s, %s, %s)
                
                ''',[ 
                    user[7]-nominal,
                    user[0],
                    uuid.uuid4(),
                    user[0],
                    date.today(),
                    -1*nominal,
                    'ec3e3a32-84b4-419a-8717-f8eae1c75f60'
                ]
            )
        
    return redirect('mypay:show_transaction_form')

# Function to render the transaction form
def view_transaction_form(request):
    context = {}
    with connection.cursor() as cursor:
        # Fetch user details based on session ID
        cursor.execute(
            '''
            select 
                * 
            from 
                public.user u
            where 
                u.id in (
                    select 
                        userid 
                    from 
                        public.session
                    where 
                        sessionid = %s
                )
            ''', [request.session['sessionId']]
        )
        user = cursor.fetchone()
        if (not user):
            return redirect('login')
        context['user'] = user
        context['logged_in'] = True

        # Check if user is a customer or worker
        cursor.execute(
        """
            select 
                * 
            from 
                public.pelanggan
            where 
                id = %s
        """, [str(user[0])])
        
        pelanggan = cursor.fetchone()
        if (pelanggan):
            context['role'] = pelanggan
            context['is_pelanggan'] = True
        else:
            cursor.execute("""
                select 
                    * 
                from 
                    public.pekerja
                where 
                    id = %s
            """, [str(user[0])])
            pekerja = cursor.fetchone()
            context['role'] = pekerja
            context['is_pelanggan'] = False
        
    return render(request, 'transaction.html', context)

# Function to render the MyPay page
def view_mypay(request):
    context = {}
    with connection.cursor() as cursor:
        # Fetch user details based on session ID
        cursor.execute(
            '''
            select 
                * 
            from 
                public.user u
            where 
                u.id in (
                    select 
                        userid 
                    from 
                        public.session
                    where 
                        sessionid = %s
                )
            ''', [request.session['sessionId']]
        )
        user = cursor.fetchone()

        if not user:
            return redirect('login')
        
        context['user'] = user
        context['logged_in'] = True

        # Check if user is a customer or worker
        cursor.execute(
        """
            select 
                * 
            from 
                public.pelanggan
            where 
                id = %s
        """, [str(user[0])])
        
        pelanggan = cursor.fetchone()
        if (pelanggan):
            context['role'] = pelanggan
            context['is_pelanggan'] = True
        else:
            cursor.execute(
                """
                select 
                    * 
                from 
                    public.pekerja
                where 
                    id = %s
                """, [str(user[0])]
            )
            pekerja = cursor.fetchone()
            context['role'] = pekerja
            context['is_pelanggan'] = False
        # Fetch transaction history for the user
        cursor.execute(
            '''
            select 
                mp.nominal, 
                mp.tgl, 
                kmp.nama 
            from 
                public.tr_mypay mp
            join 
                public.kategori_tr_mypay kmp
            on 
                kmp.id = mp.kategoriid
            where 
                mp.userid = %s
            order by 
                mp.tgl desc
            ''', [user[0]]
        )
        context['list_transaksi'] = cursor.fetchall()
    return render(request, 'mypay.html', context)