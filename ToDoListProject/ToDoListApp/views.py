from django.shortcuts import render
from django.views.generic import (ListView,DetailView,UpdateView,CreateView,DeleteView)
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
	model=Task
	context_object_name='tasks'

class TaskDetailView(DetailView):
	model=Task
	context_object_name='task'

class TaskUpdateView(UpdateView):
	model=Task
	fields='__all__'
	context_object_name='task'
	success_url=reverse_lazy('tasklist')

class TaskCreateView(CreateView):
	model=Task
	fields='__all__'
	success_url=reverse_lazy('tasklist')

class TaskDeleteView(DeleteView):
	model=Task
	context_object_name='task'
	success_url=reverse_lazy('tasklist')