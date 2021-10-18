from django.forms import ModelForm
from app.models import Paciente
from django import forms
   
class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Paciente
        fields = ['name', 'email', 'message', 'address', 'responsavel','idade']
        widgets = {
    'name': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
    'responsavel': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
    'idade': forms.DateTimeInput(
    attrs={
     'class': 'form-control',
     'type': 'date'
    }
    ),
    'address': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
   'email': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
    'message': forms.Textarea(
    attrs={
     'class': 'form-control'
     }
    ),
   }