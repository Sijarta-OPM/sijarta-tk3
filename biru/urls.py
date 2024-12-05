from django.urls import path
from biru.views import *

app_name = 'biru'

urlpatterns = [
    path('api/beli-voucher', beli_voucher, name='beli_voucher')
]