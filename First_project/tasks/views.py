from django.shortcuts import render
from django import forms

# Create your views here.

tasks = ["Answer emails", "Create my google account", "Answer Marlena"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value = 1, max_value=10)

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add_task(request):
    form = result = None
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form_user = list()
            for values in form.cleaned_data.values(): 
                form_user.append(values)
            tasks.append(form_user)
        else:
            result = "This form contains errors. Fix them: \n"
            return render(request, "tasks/add_task.html", {
                "form": form,
                "result": result
            })

    return render(request, "tasks/add_task.html", {
        "form": NewTaskForm()
    })
