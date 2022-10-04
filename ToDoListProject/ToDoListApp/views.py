from django.shortcuts import render,redirect
from django.views.generic import (ListView,DetailView,UpdateView,CreateView,DeleteView,FormView)
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class RegisterUserView(FormView):
	template_name='ToDoListApp/register.html'
	redirect_authenticated_user=True
	success_url=reverse_lazy('tasklist')
	form_class=UserCreationForm

	def form_valid(self,form):
		user=form.save()

		if user is not None:
			login(self.request,user)
		return super(RegisterUserView,self).form_valid(form)

	def get(self,*args,**kwargs):
		if self.request.user.is_authenticated:
			return redirect('tasklist')
		return super(RegisterUserView,self).get(*args,**kwargs)
class CustomLoginView(LoginView):
	template_name='ToDoListApp/login.html'
	fields='__all__'
	redirect_authenticated_user= True

	def get_success_url(self):
		return reverse_lazy('tasklist')

class TaskListView(LoginRequiredMixin,ListView):
	model=Task
	context_object_name='tasks'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks']=context['tasks'].filter(user=self.request.user)
		context['count']=context['tasks'].filter(complete=False).count()
		search_input=self.request.GET.get('search-area') or ''
		if search_input:
			context['tasks']=context['tasks'].filter(title__startswith=search_input)
		context['search_input']=search_input
		return context

class TaskDetailView(LoginRequiredMixin,DetailView):
	model=Task
	context_object_name='task'

class TaskUpdateView(LoginRequiredMixin,UpdateView):
	model=Task
	fields=['title','description','complete']
	context_object_name='task'
	success_url=reverse_lazy('tasklist')

class TaskCreateView(LoginRequiredMixin,CreateView):
	model=Task
	fields=['title','description','complete']
	success_url=reverse_lazy('tasklist')

	def form_valid(self,form):
		form.instance.user=self.request.user
		return super(TaskCreateView,self).form_valid(form)

class TaskDeleteView(LoginRequiredMixin,DeleteView):
	model=Task
	context_object_name='task'
	success_url=reverse_lazy('tasklist')