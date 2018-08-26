from django.shortcuts import render
from first_app.models import Subscriber

# Create your views here.

def index(request):
    subscriber_list = Subscriber.objects.order_by("name")
    return render(request, "first_app/index.html", {
        "subscriber" : subscriber_list
    })