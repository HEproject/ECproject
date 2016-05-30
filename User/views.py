from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/index.html', context_dict)

def login(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'page/login.html', context_dict)

# Create your views here.
