from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def servicios(request):
    return render(request,'core/servicios.html')

def experienciayclientes(request):
    return render(request,'core/experienciayclientes.html')
def contacto(request):
    return render(request,'core/contacto.html')