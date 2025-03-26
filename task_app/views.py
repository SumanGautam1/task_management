from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.views import View
from .models import Tasks
from .forms import TasksForm
from django.db.models import Q

# Create your views here.

class IndexView(CreateView):
    template_name = 'index.html'
    model = Tasks
    form_class = TasksForm
    success_url = '/index/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Passing additional data
        data['total_tasks'] = Tasks.objects.count()
        data['remaining_tasks'] = Tasks.objects.filter(Q(status='active') | Q(status = 'missed')).count()
        data['active_tasks'] = Tasks.objects.filter(status='active').count()
        data['missed_tasks'] = Tasks.objects.filter(status='missed').count()
        data['completed_tasks'] = Tasks.objects.filter(status = 'completed').count()
        data['all_task'] = Tasks.objects.all().order_by('due_date')
        data['completed_tasks_name'] = Tasks.objects.filter(status = 'completed')
        data['active_tasks_name'] = Tasks.objects.filter(Q(status='active'))
        return data
    
class DashboardView(IndexView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class MarkComplete(View):
    def post(self,request,id):
        if request.POST.get('yes'):
            model = Tasks.objects.get(id=id)
            model.status = 'completed'
            model.save()
            return redirect('index')
        else:
            return redirect('dashboard')

class ManageTask(IndexView):
    template_name = 'manage.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
    
class UpdateTask(UpdateView):
    model = Tasks
    fields = ['name', 'due_date']
    template_name = 'manage.html'
    success_url = '/manage/'

class DeleteTask(View):
    def post(self,request,id):
        data = Tasks.objects.get(id=id)
        data.delete()
        return redirect('dashboard')

