from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    UserList = User.objects.order_by("first_name")
    return render(request, "users/index.html", context={
        "user_list" : UserList
    })