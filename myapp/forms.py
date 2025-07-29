
from django import forms
from .models import Estudiante
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'carrera', 'ciclo', 'correo']
    def clean_ciclo(self):
        ciclo = self.cleaned_data.get('ciclo')
        if not ciclo.isdigit():
            raise forms.ValidationError("Debe ingresar un número.")
        return ciclo

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
