from django.shortcuts import render, redirect
 
# Create your views here.
from django import forms
from django.utils import timezone
from app.forms import MyCommentForm


def index(request):
  
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/index')
    else:
        form = MyCommentForm()
        return render(request, "cadastro2.html", {'form': form})