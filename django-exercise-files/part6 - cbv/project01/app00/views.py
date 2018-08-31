from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from app00.models import School, Student

# Create your views here.


class IndexView(TemplateView):
    template_name = "app00/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "welcome home"
        return context

class SchoolListView(ListView):
    model = School

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "List of Schools"
        return context

class StudentListView(ListView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "list of students"
        return context

class SchoolDetailView(DetailView):
    model = School

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = " Detail"
        return context
    
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age', 'school']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_header"] = "Create Student"
        return context

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = " Detail"
        return context

class SchoolCreateView(CreateView):
    model = School
    fields = ['name', 'principal', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_header"] = "Create School"
        return context

class SchoolUpdateView(UpdateView):
    model = School
    fields = ['name', 'principal', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update_header"] = "Update School"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age', 'school']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update_header"] = "Update Student"
        return context

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('school-list')
    template_name = "app00/delete.html"

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')
    template_name = "app00/delete.html"