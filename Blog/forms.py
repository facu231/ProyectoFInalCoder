from tkinter import Label
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AvatarFormulario(forms.Form):
    user = forms.CharField()
    imagen = forms.ImageField()

 
class Pedidosforms(forms.Form):
    user = forms.CharField(label = "User ")
    project = forms.CharField(label= "Ingrese un project")
    detallles = forms.CharField(label = "Detalles ")

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField( label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField( label=" Repetir la Contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        help_texts = {k : "" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label= "Modificar Nombre de usuario")
    email = forms.EmailField(label = "Modificar Mail")
    password1 = forms.CharField( label="Mofificar Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField( label=" Repetir la Contraseña modificada", widget= forms.PasswordInput)
    last_name = forms.CharField( label="Agregue su Apellido a modificar")
    first_name = forms.CharField( label="Agregue su nombre")
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2','last_name','first_name')
        help_texts = {k : "" for k in fields}

