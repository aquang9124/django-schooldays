from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Teacher, Student, Subject
# Create your views here.

class Students(TemplateView):
	template_name = 'schools/index.html'
	def get_context_data(self, **kwargs):
		return {"name": "Alex"}

class Teachers(ListView):
	model = Teacher
	template_name = 'schools/listing.html'
	def get_context_data(self, **kwargs):
		context = super(Teachers, self).get_context_data(**kwargs)
		return context

class TeacherDetailView(DetailView):
	model = Teacher
	template_name = 'schools/show.html'
	def get_context_data(self, **kwargs):
		context = super(TeacherDetailView, self).get_context_data(**kwargs)
		return context

class Subjects(ListView):
	model = Subject
	template_name = 'schools/listing.html'
	def get_context_data(self, **kwargs):
		context = super(Subjects, self).get_context_data(**kwargs)
		return context

class SubjectDetailView(DetailView):
	model = Subject
	template_name = 'schools/show.html'
	def get_context_data(self, **kwargs):
		context = super(SubjectDetailView, self).get_context_data(**kwargs)
		return context