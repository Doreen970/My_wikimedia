from django.db import models

# Create your models here.
class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=100, choices=[
        ('error', 'error'),
        ('new feature', 'new feature'),
        ('malware attack', 'malware attack'),
        ('Test Bug', 'Test Bug'),
    ])
    report_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ])

    def __str__(self):
        return self.bug_type
