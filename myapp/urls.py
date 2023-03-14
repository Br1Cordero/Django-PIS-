from django.urls import path
from . import views
urlpatterns = [
    path ('', views.Hello),
    path ('votar/', views.Votar),
    path ('estadisticas/', views.Estadisticas)
    
]