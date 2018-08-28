from django.shortcuts import render
from model_controller.models import Staff
from model_controller.forms import StaffForm

# Create your views here.
def model_controller_view(request):
    staff_list = Staff.objects.all()
    return render(request, "model.html", {
        "staff" : staff_list
    })

def model_form(request):
    staff_form = StaffForm()
    if request.method == "POST":
        staff_form = StaffForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
    return render(request, "model-form.html", {
        "form" : staff_form
    })