
from re import template
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
# Create your views here.
from django import forms
from django.utils import timezone
from app.forms import MyCommentForm, MyCommentFormchoices
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Paciente, Questionario
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy


def loginUser(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return lista(request)
    return render(request, 'logon.html', {})  


def logon(request):
    return render(request, "logon.html", {})


@login_required(login_url='../logon')
def logoutUser(request):
    logout(request) 
    return loginUser(request)

@login_required(login_url='../logon')
def index(request):
    return lista(request)

# def Questionario(request, paciente_id):
#     if request.method == "POST":
#         form = MyCommentFormchoices(request.POST)
#         if form.is_valid():
#             questionario = form.save(commit=False)
#             questionario.save()
#             return redirect('/lista')
    
#     return render(request, "questionario.html", {'form': form})


@login_required(login_url='../logon')
def lista(request):
    paciente = Paciente.objects.all()
    
    return render(request, 'lista.html', {'paciente': paciente})



class ListaPaciente(ListView):
    template_name = "lista.html"
    model = Paciente
    context_object_name = "paciente"



class PacienteUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Paciente
    fields = '__all__'
    context_object_name = 'paciente'
    success_url = reverse_lazy('lista_paciente')


class PacienteDeleteView(DeleteView):
    template_name = "exclui.html"
    model = Paciente
    fields = '__all__'
    context_object_name = 'paciente'
    success_url = reverse_lazy('lista_paciente')


class QuestionarioCreateView(CreateView):
    template_name = 'questionario.html'
    model = Questionario
    fiels = '__all__'
    form_class = MyCommentFormchoices
    success_url = reverse_lazy('lista_paciente')
        


class PacienteCreateView(CreateView):
    template_name = 'cadastro2.html'
    model = Paciente
    fiels = '__all__'
    form_class = MyCommentForm
    success_url = reverse_lazy('lista_paciente')


# def RelacionalPacienteQuestionario(request, id):
#     questionario = Questionario.objects.get(id)
#     questionario.save()
#     return render(request, 'lista.html', {'questionario':questionario})
        


def RelacionalPacienteQuestionario(request, id):
    print(id)
    paciente = Paciente.objects.get(id)
    questionario = Questionario()
    Questionario.um = request.POST.get('um')
    Questionario.dois = request.POST.get('dois')
    Questionario.tres = request.POST.get('tres')
    Questionario.quatro = request.POST.get('quatro')
    Questionario.cinco = request.POST.get('cinco')
    Questionario.seis = request.POST.get('seis')
    Questionario.sete = request.POST.get('sete')
    Questionario.oito = request.POST.get('oito')
    Questionario.nove = request.POST.get('nove')
    Questionario.dez = request.POST.get('dez')
    Questionario.onze = request.POST.get('onze')
    Questionario.dose = request.POST.get('dose')
    Questionario.treze = request.POST.get('treze')
    Questionario.quatorze = request.POST.get('quatorze')
    Questionario.quinze = request.POST.get('quinze')
    Questionario.desesseis = request.POST.get('desesseis')
    Questionario.desessete = request.POST.get('desessete')
    Questionario.dezoito = request.POST.get('dezoito')
    Questionario.dezenove = request.POST.get('dezenove')
    Questionario.vinte = request.POST.get('vinte')
    Questionario.vinteum = request.POST.get('vinteum')
    Questionario.vintedois = request.POST.get('vintedois')
    Questionario.vintetres = request.POST.get('vintetres')    
    questionario.paciente = paciente
    questionario.save()
    return render(request, 'lista.html', {'questionario':questionario})
    


def Questionariosave(request, paciente_id):
    if request.method == 'POST':

        paciente = Paciente.objects.get(pk=paciente_id)
        Questionario.um = request.POST.get('um')
        Questionario.dois = request.POST.get('dois')
        Questionario.tres = request.POST.get('tres')
        Questionario.quatro = request.POST.get('quatro')
        Questionario.cinco = request.POST.get('cinco')
        Questionario.seis = request.POST.get('seis')
        Questionario.sete = request.POST.get('sete')
        Questionario.oito = request.POST.get('oito')
        Questionario.nove = request.POST.get('nove')
        Questionario.dez = request.POST.get('dez')
        Questionario.onze = request.POST.get('onze')
        Questionario.dose = request.POST.get('dose')
        Questionario.treze = request.POST.get('treze')
        Questionario.quatorze = request.POST.get('quatorze')
        Questionario.quinze = request.POST.get('quinze')
        Questionario.desesseis = request.POST.get('desesseis')
        Questionario.desessete = request.POST.get('desessete')
        Questionario.dezoito = request.POST.get('dezoito')
        Questionario.dezenove = request.POST.get('dezenove')
        Questionario.vinte = request.POST.get('vinte')
        Questionario.vinteum = request.POST.get('vinteum')
        Questionario.vintedois = request.POST.get('vintedois')
        Questionario.vintetres = request.POST.get('vintetres')  
        Questionario.paciente = paciente
        Questionario.save()
    return render(request, 'questionario.html',{"paciente":paciente})
    
# def questionario(request, paciente_id):
#     if request.method == 'GET':
#         form = MyCommentFormchoices(request.GET)
#         if paciente_id:
#             paciente = Paciente.objects.get(pk=paciente_id)
#             return render(request, 'questionario.html', {'paciente': paciente, 'form': form})
#         return render(request, 'questionario.html', {'form': form})
#     if request.method == "POST":
#         form = MyCommentFormchoices(request.POST)
#         if form.is_valid():
#             model_instancechoices = form.save(commit=False)
#             model_instancechoices.save()
#             return redirect('/lista')
#     else:
#         form = MyCommentFormchoices()
#         return render(request, "questionario.html", {'form': form})


def Salvaquestionario(request, paciente_id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(pk=paciente_id)
        form = MyCommentFormchoices(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("lista.html", {'form': form})
    else:
        form = MyCommentFormchoices()
    return render(request, 'lista.html',)