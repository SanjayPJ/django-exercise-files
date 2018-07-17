from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
     my_dict = {"insert_me" : "Something that is common in both file"}
     return render(request , 'app0/index.html', context=my_dict)
