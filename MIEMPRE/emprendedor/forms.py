from django import forms
from .models import Emprendimiento

class emprendimientoForm(forms.ModelForm):
    
    class Meta:
        model = Emprendimiento
        fields = '__all__'
