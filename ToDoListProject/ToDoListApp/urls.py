from django.urls import path
from .views import TaskListView,TaskDetailView,TaskUpdateView,TaskDeleteView,TaskCreateView

#app_name='ToDoListApp'
urlpatterns=[
	path('',TaskListView.as_view(),name='tasklist'),
	path('task/<int:pk>/',TaskDetailView.as_view(),name='taskdetail'),
	path('Update/<int:pk>/',TaskUpdateView.as_view(),name='taskupdate'),
	path('Create/',TaskCreateView.as_view(),name='taskcreate'),
	path('Delete/<int:pk>/',TaskDeleteView.as_view(),name='taskdelete')
] 