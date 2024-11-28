from django.urls import path
from hijau.views import *
app_name = 'hijau'

urlpatterns = [
    path('<uuid:id>', view_subkategori_jasa, name='show_subkategori'),
]