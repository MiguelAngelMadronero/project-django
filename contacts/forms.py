from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields =['nombre', 'numero', 'descripcion', 'relevante']
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un nombre...' }),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un número...' }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción...' }),
            'relevante': forms.CheckboxInput(attrs={'class': 'form-check-input' }),

        }