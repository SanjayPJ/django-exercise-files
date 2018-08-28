from django.shortcuts import render
from form_controller.forms import User

# Create your views here.

def form_controller_views(request):
    user = User()
    if request.method == "POST":
        user = User(request.POST)
        if user.is_valid():
            print(user.cleaned_data["name"])
            print(user.cleaned_data["email"])
            print(user.cleaned_data["url"])
    return render(request, "form.html", {
        "user" : user
    })