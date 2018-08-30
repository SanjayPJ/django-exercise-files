from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from basic_app.models import School, Student


# Create your views here.

class DemoView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inject_var"] = "This is what i need to inject!"
        return context
    
class SchoolListView(ListView):
    context_object_name = "schools"
    model = School
    template_name = "basic_app/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = "school_details"
    model = School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    model = School
    fields = ("name", "principal", "location")
    # template_name = "TEMPLATE_NAME"
