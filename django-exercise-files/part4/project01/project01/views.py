from django.shortcuts import render
from . import forms

def index(request):
    form = forms.Demo()
    if request.method == "POST":
        form = forms.Demo(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
    return render(request, "index.html", {
        "form" : form
    })