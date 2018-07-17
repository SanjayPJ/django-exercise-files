from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     my_dict = {'insert_me' : "This text is imported from index : views.py"}
     return render(request, 'app/index.html', context=my_dict)

def helper(request):
     my_dict = {'insert_me' : "This text is imported from help : views.py"}
     return render(request, 'app/help.html', context=my_dict)
