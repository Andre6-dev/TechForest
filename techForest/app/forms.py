from django import forms  
from api.models import * 
class ErrorForm(forms.ModelForm):  
    class Meta:  
        model = Errores  
        fields = ["titulo","mensaje",]  

class UsuarioForm(forms.ModelForm):  
    class Meta:  
        model = Profile  
        fields = ["nombres","apellidos","correo","contraseña"]  

class LoginCliente(forms.ModelForm):
    class Meta: 
        model = Profile  
        fields = ["correo","contraseña"]