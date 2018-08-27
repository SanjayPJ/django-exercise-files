from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app00/index.html", {
        "text" : "Hello World",
        "number" : 100
    })

def other(request):
    return render(request, "app00/other.html")

def relative(request):
    return render(request, "app00/relative_url_templates.html")