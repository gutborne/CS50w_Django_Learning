from django.shortcuts import render

# Create your views here.
def index(request):
    tasks = ["Answer emails", "Create my google account", "Answer Marlena"]
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add_task(request):
    return render(request, "tasks/add_task.html")
