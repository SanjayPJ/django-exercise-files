from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html", context={
        "content_header" : "Welcome!",
        "content_para" : "gotp /users to see the list of user info."
    })