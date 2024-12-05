from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from main.views import get_user, get_pelanggan, get_pekerja, logout
import json
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

    context = {
        'logged_in' : True,
        'user' : user,
        'role' : role,
        'is_pelanggan' : is_pelanggan,
        'voucher' : voucher,
        'promo' : promo
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
    # we will perform insert query on public.tr_pembelian_voucher
    # beli_voucher should be call if the request method is POST, so to get data from body
    # we are expecting voucher code, user's id, and 
    # if user fill with 
    data = json.loads(request.body)

    kode = data.get('kodevoucher')
    harga_voucher = data.get('harga_voucher')
    saldo_user = user[7]
    if (harga_voucher > saldo_user):
        return JsonResponse({
            'status' : 'success',
            'buy_status' : 'failed'
        })
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                insert into public.tr_pembelian_voucher
                values (%s, %s, %s, %s, %s, %s, %s)
                ''', []
            )


