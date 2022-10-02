from django.urls import path
from .views import TaskListView,TaskDetailView,TaskUpdateView,TaskDeleteView,TaskCreateView,CustomLoginView,RegisterUserView
from django.contrib.auth.views import LogoutView

#app_name='ToDoListApp'
urlpatterns=[
	path('Register/',RegisterUserView.as_view(),name='register_user'),
	path('Login/',CustomLoginView.as_view(),name='login'),
	path('Logout/',LogoutView.as_view(next_page='login'),name='logout'),
	path('',TaskListView.as_view(),name='tasklist'),
	path('task/<int:pk>/',TaskDetailView.as_view(),name='taskdetail'),
	path('Update/<int:pk>/',TaskUpdateView.as_view(),name='taskupdate'),
	path('Create/',TaskCreateView.as_view(),name='taskcreate'),
	path('Delete/<int:pk>/',TaskDeleteView.as_view(),name='taskdelete')
] 