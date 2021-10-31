from django.shortcuts import render, redirect
 
# Create your views here.
from django import forms
from django.utils import timezone
from app.forms import MyCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Paciente


def loginUser(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
    return render(request, 'app/login.html', {})  

@login_required(login_url='../login')
def logoutUser(request):
    logout(request) 
    return loginUser(request)


@login_required(login_url='../login')
def index(request):
    return render(request, 'app/index.html', {'user': request.user })


def cadastro(request):
  
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/cadastro')
    else:
        form = MyCommentForm()
        return render(request, "cadastro2.html", {'form': form})


@login_required(login_url='../login')

def Lista(request):
    paciente = Paciente.objects.all()
    
    return render(request, 'lista.html', {'paciente': paciente})



