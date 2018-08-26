from django.shortcuts import render
from django.http import HttpResponse
from app00.models import User

# Create your views here.
def index(request):
    return HttpResponse("Goto /app00 to view user details")

def user(request):
    form_data = User.objects.all()
    return render(request, "index.html", {
        "form_data" : form_data
    })