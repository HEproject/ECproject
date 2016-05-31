from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/index.html', context_dict)

def login(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/login.html', context_dict)

def test(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/test.html', context_dict)

def register(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/register.html', context_dict)

def base(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/base.html', context_dict)

# Create your views here.
