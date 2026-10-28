from django.shortcuts import render
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value = 1, max_value=10)

def index(request):
    tasks = ["Answer emails", "Create my google account", "Answer Marlena"]
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add_task(request):
    return render(request, "tasks/add_task.html", {
        "form": NewTaskForm()
    })
