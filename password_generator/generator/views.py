from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/index.html')

def password(request):
    return render(request, 'generator/password.html')

def generated(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase') :
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers') :
        characters.extend(list('1234567890'))
    if request.GET.get('special') :
        characters.extend(list('!@#$%^&*()'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/generated.html',{'password': thepassword})
