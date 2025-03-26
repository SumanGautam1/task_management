from django.db import models
from datetime import datetime

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    status_choices = (
        ('completed', 'completed'),
        ('active', 'active'),
        ('missed', 'missed') 
    )

    status = models.CharField(choices=status_choices, default='active', max_length=20)
    days_left = models.IntegerField(editable=False)
    priority = models.IntegerField(default=1, editable=False)

    def save(self, *args, **kwargs):
        self.days_left = (self.due_date - datetime.now().date()).days
        if self.days_left < 0:  # Overdue tasks get the highest priority
            self.priority = 5
        elif self.days_left <= 5:
            self.priority = 4
        elif self.days_left <= 10:
            self.priority = 3
        elif self.days_left <= 20:
            self.priority = 2
        else:
            self.priority = 1

        if self.days_left <= 0:
            self.status = 'missed'
        return super().save(*args, **kwargs)
    

    
    class Meta:
        ordering = ['-priority', 'due_date']  # Higher priority first, then closest due date

    def __str__(self):
        return self.name

    

