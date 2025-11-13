from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('catalogomujer/', views.catalogo_mujer, name='catalogo_mujer'),
    path('catalogohombre/', views.catalogo_hombre, name='catalogo_hombre'),
    path('catalogoninos/', views.catalogo_ninos, name='catalogo_ninos'),
]