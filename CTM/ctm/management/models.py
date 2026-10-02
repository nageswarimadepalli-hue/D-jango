from django.db import models

# Create your models here.

class Course(models.Model):
    c_name=models.CharField(max_length=100)
    c_duration=models.IntegerField()
    c_fees=models.IntegerField()
    triner_name=models.CharField(max_length=100)
    start_date=models.DateField()
    number_seats=models.IntegerField()
    active_course=models.BooleanField(default=True)
    

    