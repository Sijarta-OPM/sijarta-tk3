from django.urls import path
from main.views import *
from biru.views import show_diskon_page
urlpatterns=[
    path('', show_homepage, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/<uuid:id>', show_profile, name='profile'),
    path('pekerjaan-jasa/', view_pemesanan_jasa, name='pekerjaan_jasa'),
    path('status-pekerjaan-jasa/',view_status_pemesanan_jasa, name='status_pekerjaan_jasa'),
    path('diskon/', show_diskon_page, name='diskon'),
    path('api/subkategori/<uuid:id>', show_subkategori_by_id, name='subkategori'),
    path('api/kategori/<uuid:id>', show_kategori_by_id, name='kategori'),
    path('api/search-subkategori/', search_subkategori, name="search"),
    path('api/get-subkategori-pemesanan/',get_subkategori_pemesanan, name='subkategori_pemesanan'),
    path('api/get-pemesanan/', get_pemesanan, name="get_pemesanan"),
    path('api/get-status-pemesanan/', get_status_pemesanan, name="get_stasus_pemesanan"),
    path('api/kerjakan-pemesanan-jasa/', kerjakan_pemesesanan_jasa),
    path('api/update-status-pemesanan/', update_status_pemesanan, name="update_status_pemesanan")
]