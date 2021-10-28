from django.forms import ModelForm
from app.models import Paciente
from django import forms
   
class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Paciente
        fields = ['name', 'email', 'message', 'address', 'responsavel','idade','phone']
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
    'phone': forms.TextInput(
    attrs={
     'class': 'form-control',
     'placeholder': '(99) 99999-9999',
     'id': 'telefone',
     'name': 'telefone'
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