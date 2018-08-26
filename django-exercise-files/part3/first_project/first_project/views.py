from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html", {
        "post" : ["goto /first_app to find user details",
                  "goto /form_app to check out the form", 
                  ],
    })