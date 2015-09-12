from django.db import models

# Create your models here.
class Attendees(models.Model):
    student_name = models.CharField(max_length=100)
    attend_date = models.DateTimeField(auto_now_add=True)
