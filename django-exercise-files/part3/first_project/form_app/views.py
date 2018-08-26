from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = forms.Sample(request.POST)

        if form.is_valid():
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["message"])

    form = forms.Sample()
    return render(request, "form_app/index.html", {
        "form" : form.as_p
    })