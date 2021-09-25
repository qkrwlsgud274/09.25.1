from django.db import models

# Create your models here.


class Data(models.Model):
    Email = models.CharField(max_length=30, null=False)
    Password = models.CharField(max_length=30, null=False)
