from django.shortcuts import render, redirect
from .models import Emprendimiento
from . import forms

# Create your views here.
def probando(request):
    emprendmiento = Emprendimiento.objects.all()
    data = {'emprendimientos': emprendmiento}
    return render(request, "emprendedor/emprendimientos.html", data)


def agregarEmprendimiento(request):
    form = forms.emprendimientoForm()
    if request.method == 'POST':
        form = forms.emprendimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('lista_emprendimiento')
    data = {'form': form}
    return render(request, 'emprendedor/agregarEmpren.html', data)


def actualizarEmprendimiento(request, id):
    emprendimiento = Emprendimiento.objects.get(id=id)
    form = forms.emprendimientoForm(instance=emprendimiento)
    if request.method == 'POST':
        form = forms.emprendimientoForm(request.POST, instance=emprendimiento)
        if form.is_valid():
            form.save()
        return redirect('lista_emprendimiento')
    data = {'form': form}
    return render(request, 'emprendedor/agregarEmpren.html', data)


def eliminarEmprendimiento(request, id):
    emprendimiento = Emprendimiento.objects.get(id=id)
    emprendimiento.delete()
    return redirect('lista_emprendimiento')