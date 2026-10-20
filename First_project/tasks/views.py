from django.shortcuts import render

# Create your views here.
def index(request):
    tasks = ["Answer emails", "Create my google account", "Answer Marlena"]
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
