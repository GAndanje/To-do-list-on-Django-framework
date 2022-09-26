from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Task

# Create your views here.
class TaskListView(ListView):
	model=Task
	context_object_name='tasks'
class TaskDetailView(DetailView):
	model=Task