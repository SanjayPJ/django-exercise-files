from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    AccessRecordList = AccessRecord.objects.order_by("date")
    return render(request, "index.html", context={
        "access_records" : AccessRecordList
        })