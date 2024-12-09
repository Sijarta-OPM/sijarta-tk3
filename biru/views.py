from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from main.views import get_user, get_pelanggan, get_pekerja, logout
import json
import uuid

# Create your views here.
def show_diskon_page(request):
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('home')
    logged_in = True
    
    role = get_pelanggan(user[0])
    is_pelanggan = True
    if (not role):
        logout()
        return redirect('home')
    
    voucher = get_voucher()
    promo = get_promo()
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.metode_bayar
            '''
        )
        metode_bayar = cursor.fetchall()
    
    context = {
        'logged_in' : True,
        'user' : user,
        'role' : role,
        'is_pelanggan' : is_pelanggan,
        'voucher' : voucher,
        'promo' : promo,
        'metode_bayar' : metode_bayar
    }
    return render(request, 'diskon.html', context)

def get_promo():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.promo
            '''
        )
        return cursor.fetchall()

def get_voucher():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.voucher
            '''
        )
        return cursor.fetchall()
    
def beli_voucher(request):
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('home')
    pelanggan = get_pelanggan(user[0])
    if (not pelanggan):
        return redirect('home')
    data = json.loads(request.body)

    kode = data.get('kode_voucher')
    harga_voucher = data.get('harga_voucher')
    metode_bayar = data.get('payment_method')

    success = False
    
    print(kode)
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.voucher where kode = %s
            ''', [kode]
        )
        voucher = cursor.fetchone()

    if metode_bayar != 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb':
        success = True
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                insert into public.tr_pembelian_voucher(id, tglawal, tglakhir, telahdigunakan, idpelanggan, idvoucher, idmetodebayar)
                values (
                    %s, NOW(), NOW() + INTERVAL %s , 0, %s, %s, %s
                )
                ''', [str(uuid.uuid4()),   f'{voucher[1]} days', user[0], kode, metode_bayar ]
            )
    else:
        saldo_user = user[7]
        if float(saldo_user) >= float(harga_voucher):
            success = True
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    insert into public.tr_pembelian_voucher
                    values (
                        %s, NOW(), NOW() + INTERVAL %s , 0, %s, %s, %s
                    )
                    ''', [uuid.uuid4(), f'{voucher[1]} days', user[0], kode, metode_bayar ]
                )
                cursor.execute(
                    '''
                    update public.user
                    set saldomypay = saldomypay - %s
                    where id = %s
                    ''', [harga_voucher, user[0]]
                )
    return JsonResponse({
        'status' : 'success',
        'buy_status' : success,
        'voucher' : voucher
    })


