from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):

    if request.method == "POST":
        form = forms.DEMO_FORM2(request.POST)
        if form.is_valid():
            print(form.cleaned_data["first_name"])
            print(form.cleaned_data["last_name"])
            print(form.cleaned_data["address_1"])
            print(form.cleaned_data["address_2"])
            print(form.cleaned_data["website"])
            print(form.cleaned_data["pin"])
            

    form = forms.DEMO_FORM2()
    return render(request, "form_app2/index.html", {
        "form" : form
    })