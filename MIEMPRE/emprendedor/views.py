from django.shortcuts import render
from .models import Emprendimiento
from . import forms

# Create your views here.
def probando(request):
    emprendmiento = Emprendimiento.objects.all()
    data = {'emprendimientos': emprendmiento}
    return render(request, "emprendedor/emprendimientos.html", data)


def agregarEmprendimiento(request):
    form = forms.formEmprendimiento()


    if request.method == 'POST':
        form = forms.formEmprendimiento(request.POST)
        if form.is_valid():
            emprendimiento = form.save(commit=False)
    data = {'form': form}
    return render(request, 'emprendedor/agregarEmpren.html', data)