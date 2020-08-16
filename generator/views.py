from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters='abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('uppercase'):
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if request.GET.get('special'):
        characters += '!@#$%^&*,.'
    if request.GET.get('numbers'):
        characters += '0123456789'
    if request.GET.get('numbers_only'):
        characters = '0123456789'
    length=int(request.GET.get('length',12))
    res = ''
    for i in range(length):
        res += random.choice(characters)
    return render(request, 'generator/password.html', {'password': res})


def about(request):
    return render(request, 'generator/about.html')