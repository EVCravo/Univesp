
from django.forms import ModelForm
from django.forms.widgets import RadioSelect
from app.models import Paciente, Questionario
from django import forms

# class FotoForm(forms.Form):
#     model = FotoModel
#     foto = forms.ImageField(
#         required=False,
#         widget=forms.ClearableFileInput(attrs={'multiple': True})
#     )

#     class Meta:
#         model = Paciente
#         fields = ('foto')

#     def __init__(self, *args, **kwargs):
#         super(FotoForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#         self.fields['photo'].widget.attrs['class'] = None

   
class MyCommentFormchoices(forms.ModelForm):
    class Meta(object):
        #escolha = (('Sim', 'Sim'), ('Não', 'Não'))
        model = Questionario
        fields = '__all__'
        
        

class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Paciente
        fields = ['name', 'email', 'message', 'rua','responsavel','idade','phone','prontuario', 'name','cpf','cep', 'bairro','cidade',]
        widgets = {

    

    'name': forms.TextInput(
    attrs={
     'class': 'form-control',
     'pattern':"[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$"
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
    'rua': forms.TextInput(
    attrs={
     'class': 'form-control',
     'type': 'text',
     'id': 'rua',
     'name': 'rua',
     'size': '60',
     'value':"",
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
    'prontuario': forms.TextInput(
    attrs={
    'class': 'form-control',
    'type': 'int',
    'name': 'prontuario',
    'id' : 'prontuario'
    }
    ),
    'cpf': forms.TextInput(
    attrs={
    'placeholder':'xxx.xxx.xxx-xx',
    'class': 'form-control',
    'type': 'int'
    }
    ),
    'cep': forms.TextInput(
    attrs={
     'class': 'form-control',
     'type': 'text',
     'placeholder': '00000-000',
     'size' : "10",
     'maxlength' : "9",
     'id': 'cep',
     'name': 'cep',
     
     }
    ),
    'bairro': forms.TextInput(
    attrs={
     'class': 'form-control',
     'type': 'text',
     'id': 'bairro',
     'name': 'bairro',
     'size': '50',
     }
    ),
    'cidade': forms.TextInput(
    attrs={
     'class': 'form-control',
     'type': 'text',
     'id': 'cidade',
     'name': 'cidade',
     'size': '50',
     }
    ),
   }
    

  