from django.urls import path
from .views import TaskListView,TaskDetailView

urlpatterns=[
	path('',TaskListView.as_view(),name='tasklist'),
	path('task/<int:pk>',TaskDetailView.as_view(),name='taskdetail')
]