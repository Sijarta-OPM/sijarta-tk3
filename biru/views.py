from django.shortcuts import render, redirect
from django.db import connection
from main.views import get_user, get_pelanggan, get_pekerja, logout

# Create your views here.
def show_diskon_page(request):
    user = get_user(request.session['sessionId'])
    if (not user):
        return redirect('login')
    logged_in = True
    
    role = get_pelanggan(user[0])
    is_pelanggan = True
    if (not role):
        logout()
        return redirect('login')
    
    context = {
        'logged_in' : True,
        'user' : user,
        'role' : role,
        'is_pelanggan' : is_pelanggan
    }
    return render(request, 'diskon.html', context)

def get_promo():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.promo
            '''
        )
    return

def get_diskon():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            select * from public.voucher
            '''
        )
    return