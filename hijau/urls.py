from django.urls import path
from hijau.views import *
app_name = 'hijau'

urlpatterns = [
    path('<uuid:id>', view_subkategori_jasa, name='show_subkategori'),
    path('api/add-pemesanan-jasa', add_pemesanan_jasa, name="add_pemesanan_jasa"),
    path('api/check_diskon', check_diskon, name="check_diskon"),
    path('api/get-already-join/', get_already_join, name='get_already_join'),
    path('api/gabungkan-pekerja/', gabungkan_pekerja, name="gabungkan_pekerja")
]