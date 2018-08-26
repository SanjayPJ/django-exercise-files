from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, "home/index.html", {

    })

def sign_up(request):
    sign_up_form = forms.SignUpPage()

    if request.method == "POST":
        sign_up_form = forms.SignUpPage(request.POST)

        if sign_up_form.is_valid():
            print(sign_up_form.cleaned_data['first_name'])
            print(sign_up_form.cleaned_data['last_name'])
            print(sign_up_form.cleaned_data['email'])
            print(sign_up_form.cleaned_data['password'])

    return render(request, "sign_up/index.html", {
        "sign_up_form" : sign_up_form.as_p
    })