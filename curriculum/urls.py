from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
        path('home/', views.home, name='home'),
        path('experiencia/', views.experiencia, name='experiencia'),
        path('estudios/', views.estudios, name='estudios'),
        path('habilidades/', views.habilidades, name='habilidades'),
        path('hobbies/', views.hobbies, name='hobbies'),
        path('contacto/', views.contacto, name='contacto'),
        path('', lambda request: redirect('home/')),
]