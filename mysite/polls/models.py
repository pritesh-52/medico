from django.db import models


class Patient(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField(max_length=12)
    date=models.DateField()
    message=models.TextField()
