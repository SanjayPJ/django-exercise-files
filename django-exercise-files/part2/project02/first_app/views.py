from django.shortcuts import render
from first_app.models import User

# Create your views here.
def index(request):
    UserList = User.objects.order_by("name")
    return render(request, "first_app/bootstrap-template.html", context={
        "user_list" : UserList
    })