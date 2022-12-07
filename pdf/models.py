from django.db import models
from datetime import date

# Create your models here.

class Profile(models.Model):
    company_name=models.CharField(max_length=100)
    company_addr=models.CharField(max_length=100)
    your_name=models.CharField(max_length=100)
    your_addr=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    campus_name=models.CharField(max_length=100)
    skill=models.TextField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    d_year=models.CharField(max_length=100,null=True)
    d_month=models.CharField(max_length=100,null=True)
    d_day=models.CharField(max_length=100,null=True)
    image=models.ImageField(null=True,blank=True)
            

