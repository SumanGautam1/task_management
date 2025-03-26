from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('index/', IndexView.as_view(), name='index'),
    path('mark_complete/<int:id>', MarkComplete.as_view(), name='mark_complete'),
    path('manage/', ManageTask.as_view(), name='manage'),
    path('delete/<int:id>', DeleteTask.as_view(), name='delete_task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update_task'),
]