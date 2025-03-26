from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'due_date']

        widgets = {
            'name' : forms.TextInput(attrs={
                'class':'form-control form-control-lg', 
                'placeholder':'Enter the task name...'
                }),
            'due_date' : forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'
            })
        }