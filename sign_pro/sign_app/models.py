from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

class signupdata(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
