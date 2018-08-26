from django.shortcuts import render
from app01.forms import CreateUserFormForm

# Create your views here.

def index(request):

    

    if request.method == "POST":

        form = CreateUserFormForm(request.POST)

        if form.is_valid():

            form.save()

    form = CreateUserFormForm()

    return render(request, 'form.html', {
        "form" : form
    })