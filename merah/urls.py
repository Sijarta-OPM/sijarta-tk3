from django.urls import path
from merah.views import *

app_name = 'merah'

urlpatterns = [
    path('transaksi/', view_transaction_form, name="show_transaction_form"),
    path('transfer/', transfer, name="transfer"),
    path('payment/', payment, name="payment"),
    path('topup/', topup, name="topup"),
    path('withdraw/', withdraw, name="withdraw"),
    path('api/get-order', get_order, name="get_order"),
    path('', view_mypay, name='show_mypay')
]