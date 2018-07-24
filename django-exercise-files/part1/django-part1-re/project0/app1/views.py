from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    content = {
        'psudoname' : 'bingo6'
    }
    return render(request, 'about.html', content)