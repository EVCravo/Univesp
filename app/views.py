
from django.shortcuts import render, redirect
 
# Create your views here.
from django import forms
from django.utils import timezone
from app.forms import MyCommentForm, MyCommentFormchoices
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Paciente, Questionario

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

def cadastro(request):
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/lista')
    else:
        form = MyCommentForm()
        return render(request, "cadastro2.html", {'form': form})


@login_required(login_url='../logon')
def lista(request):
    paciente = Paciente.objects.all()
    
    return render(request, 'lista.html', {'paciente': paciente})





# def questionario(request):
#     paciente = Paciente.objects.get()
#     Questionario.um = request.POST.get('um')
#     Questionario.dois = request.POST.get('dois')
#     Questionario.tres = request.POST.get('tres')
#     Questionario.quatro = request.POST.get('quatro')
#     Questionario.cinco = request.POST.get('cinco')
#     Questionario.seis = request.POST.get('seis')
    
    
    
#     Questionario.paciente = paciente
#     Questionario.save()
#     return render(request, 'questionario.html',{"paciente":paciente})
    
def questionario(request, paciente_id):
    if request.method == 'GET':
        form = MyCommentFormchoices(request.GET)
        if paciente_id:
            paciente = Paciente.objects.get(pk=paciente_id)
            return render(request, 'questionario.html', {'paciente': paciente, 'form': form})
        return render(request, 'questionario.html', {'form': form})
    if request.method == "POST":
        form = MyCommentFormchoices(request.POST)
        if form.is_valid():
            model_instancechoices = form.save(commit=False)
            model_instancechoices.timestamp = timezone.now()
            model_instancechoices.save()
            return redirect('/lista')
    else:
        form = MyCommentFormchoices()
        return render(request, "cadastro2.html", {'form': form})