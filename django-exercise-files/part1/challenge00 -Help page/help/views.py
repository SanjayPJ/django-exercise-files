from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "help/index.html", context={
        "page_name" : "HELP"
    })