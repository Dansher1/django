from django.db import models

# Create your models 

class Student(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    image = models.FileField(upload_to='users/',null=True)


