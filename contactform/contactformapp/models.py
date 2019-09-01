from django.db import models

class EmpDATA(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)

