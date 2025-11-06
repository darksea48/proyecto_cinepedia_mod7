from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'director', 'fecha_estreno', 'sinopsis']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_estreno': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ComentarioForm(forms.Form):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label='Comentario'
    )