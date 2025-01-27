from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def experiencia(request):
    return render(request, 'experiencia.html')

def estudios(request):
    return render(request, 'estudios.html')

def habilidades(request):
    return render(request, 'habilidades.html')

def hobbies(request):
    return render(request, 'hobbies.html')

def contacto(request):
    return render(request, 'contacto.html')
