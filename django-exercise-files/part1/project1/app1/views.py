from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     my_dict = {'insert_me' : "This text is imported from views.py"}
     return render(request, 'app1/index.html', context=my_dict)
