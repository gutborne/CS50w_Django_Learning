from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!!")

def mateus(request):
    return HttpResponse("Hello, Mateus!")

def zuzia(request):
    return HttpResponse("hello, Zuzia!")

def Marlena(request):
    return HttpResponse("hello, Marlena!")

def greetings_user(request, user):
    return HttpResponse(f"Hello, {user.capitalize()}!!")



