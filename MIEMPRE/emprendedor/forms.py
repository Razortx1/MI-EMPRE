from django import forms
from .models import Emprendimiento

class formRegistration(forms.Form):
    nombreProyecto = forms.CharField(max_length=50)
    detalleEmprendimiento = forms.CharField(max_length=1000)
    imagenEmprendimiento = forms.CharField(max_length=250)
    estadoEmprendimiento = forms.CharField(max_length=50)

class formEmprendimiento(forms.ModelForm):
    class meta:
        model = Emprendimiento
        fiels = '__all__'