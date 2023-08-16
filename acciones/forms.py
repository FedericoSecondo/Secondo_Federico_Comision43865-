from django import forms
from .models import Accion
from .models import CEOEmpresa
from .models import ResultadoEconomico
from .models import ETF
from .models import bkn
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#----------------------------------------------------------------------------------------------
#  AQUI SE DETALLAN LOS FORMULARIOS CREADOS QUE PERMITEN CREAR NUEVOS DATOS PARA CADA MODELO
#----------------------------------------------------------------------------------------------

class AgregarAccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ['simbolo', 'descripcion', 'fecha_fundacion']


class CEOEmpresaForm(forms.ModelForm):
    class Meta:
        model = CEOEmpresa
        fields = ['accion', 'nombre_director', 'nacionalidad', 'sitio_web']

    def clean_sitio_web(self):
        sitio_web = self.cleaned_data['sitio_web']
        return sitio_web
    


class ResultadoEconomicoForm(forms.ModelForm):
    class Meta:
        model = ResultadoEconomico
        fields = ['accion_comprada', 'resultado_ultimo_anio', 'proyeccion_proximo_anio']

class ETFForm(forms.ModelForm):
    class Meta:
        model = ETF
        fields = ['simbolo', 'nombre', 'subyacente', 'precioTarget']

class BKNForm(forms.ModelForm):
    class Meta:
        model = bkn
        fields = ['empresa', 'titular']


class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}   

#ediciond e usuarios:

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}

#------------------------------------------------------------------------------
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True) 



