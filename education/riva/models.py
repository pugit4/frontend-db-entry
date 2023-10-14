from django.db import models

# Create your models here.
class students_details(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=45)
    grade = models.CharField(max_length=40)
    standard = models.IntegerField()
    
    