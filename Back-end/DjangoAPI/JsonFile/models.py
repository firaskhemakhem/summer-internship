from django.db import models
# import jsonfield

# Create your models here.

class User (models.Model):
    Login = models.CharField(max_length= 30,primary_key=True)
    Email = models.CharField(max_length= 30,unique=True)

class JsonfileModel (models.Model):
    Name = models.CharField(max_length= 30,primary_key=True)
    Details = models.JSONField()