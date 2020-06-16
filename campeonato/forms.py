from django.contrib.auth.forms import AuthenticationForm
from .models import Equipo, Entrenador, Jugador, Juega, Partidos, Liga
from django import forms

class FormularioLogin(AuthenticationForm):
    def init(self, args, **kwargs):
        super(FormularioLogin, self).init(args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['foto', 'nombre', 'presupuesto', 'presidente', 'estadio', 'titulos', 'id_liga']
        labels = {
             'nombre': 'Nombre del equipo',
             'presupuesto': 'Presupuesto',
             'presidente': 'Presidente',
             'estadio': 'Estadio',
             'titulos': 'Títulos',
        }
        widgets = {
             'foto': forms.FileInput(
                 attrs={
                     'class':'form-control'
                 }
             ),
             'nombre': forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Nombre del equipo'
                 }
             ),
             'presupuesto': forms.NumberInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Presupuesto'
                 }
            ),
             'presidente':forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Nombre del presidente'
                 }
             ),
             'estadio': forms.TextInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Nombre del estadio'
                 }
             ),
             'titulos':forms.NumberInput(
                 attrs={
                     'class':'form-control',
                     'placeholder':'Títulos'
                 }
             ),
             'id_liga':forms.Select(
                 attrs={
                     'class':'form-control'
                 }
             )
         }

class JugadorForm(forms.ModelForm):
    class Meta:
         model = Jugador
         fields = ['foto', 'nombre', 'apellidos', 'pais', 'f_nacimiento', 'posicion', 'id_equipo']
         labels = {
             'nombre': 'Nombre del jugador',
             'apellidos': 'Apellidos',
             'pais': 'País',
             'f_nacimiento': 'Fecha de Nacimiento',
             'posicion': 'Posición',
         }

         widgets = {
             'foto': forms.FileInput(
                 attrs={'class':'form-control'
                  }
              ),
              'nombre': forms.TextInput(
                 attrs={
                      'class':'form-control',
                      'placeholder':'Nombre del jugador'
                  }
              ),
              'apellidos': forms.TextInput(
                  attrs={
                      'class':'form-control',
                      'placeholder':'Apellidos'
                  }
              ),
              'pais':forms.TextInput(
                  attrs={
                      'class':'form-control',
                      'placeholder':'País'
                  }
              ),
              'f_nacimiento': forms.DateInput(
                  format= '%d/%m/%Y', 
                  attrs={
                      'class':'form-control'
                  }
              ),
              'posicion':forms.TextInput(
                  attrs={
                      'class':'form-control',
                      'placeholder':'Posición'
                  }
              ),
              'id_equipo':forms.Select(
                  attrs={
                      'class':'form-control'
                  }
              )
         }