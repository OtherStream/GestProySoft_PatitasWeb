# avisos/forms.py

from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        # Incluye todos los campos excepto la fecha de creación, que es automática
        fields = ['nombre', 'tipo', 'descripcion', 'imagen'] 
        
        # Widgets para aplicar clases de estilo (ej. Bootstrap)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }