from django.urls import path
from . import views

app_name = 'home_edgardo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<str:genero_id>/', views.peliculas_por_genero, name='peliculas'),
]