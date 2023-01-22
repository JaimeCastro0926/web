from django.urls import path

from . import views

urlpatterns = [
   path('index/', views.index, name='index'),
   path('salir/', views.index, name='salir'),
   path('chao/', views.index, name='chao'),
]