from django.urls import path
from main.views import *
urlpatterns=[
    path('', show_homepage, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/<uuid:id>', show_profile, name='profile'),
    path('api/subkategori/<uuid:id>', show_subkategori_by_id, name='subkategori'),
    path('api/kategori/<uuid:id>', show_kategori_by_id, name='kategori'),
    path('api/search-subkategori/', search_subkategori, name="search"),
    path('pekerjaan-jasa/', view_pemesanan_jasa, name='pekerjaan_jasa'),
    path('status-pekerjaan-jasa/',view_status_pemesanan_jasa, name='status_pekerjaan_jasa')
]