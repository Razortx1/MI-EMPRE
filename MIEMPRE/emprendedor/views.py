from django.shortcuts import render
from .models import Emprendimiento
from . import forms

# Create your views here.
def probando(request):
    emprendmiento = Emprendimiento.objects.all()
    data = {'emprendimientos': emprendmiento}
    return render(request, "emprendedor/emprendimientos.html", data)


def agregarEmprendimiento(request):
    return render(request, 'emprendedor/agregarEmpren.html')