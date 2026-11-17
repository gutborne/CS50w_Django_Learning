from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value = 1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add_task(request):
    form = result = None
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form_user = list()
            for value in form.cleaned_data.values(): 
                form_user.append(value)
            request.session["tasks"].append(form_user)
            request.session.modified = True
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            result = "This form contains errors. Fix them: \n"
            return render(request, "tasks/add_task.html", {
                "form": form,
                "result": result
            })

    return render(request, "tasks/add_task.html", {
        "form": NewTaskForm()
    })
