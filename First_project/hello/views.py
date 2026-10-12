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

#rendering html files with render function
#the third argument in render function is called 'context'
def greetings_user(request, user):
    return render(request, "hello/index.html", {
        "user": user.capitalize()
    })



