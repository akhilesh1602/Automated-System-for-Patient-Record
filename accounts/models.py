from django.db import models
from django.contrib.auth.models import AbstractUser



class User1(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

class Patient(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    #class_name = models.CharField(max_length=100)

class Doctor(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    #department = models.CharField(max_length=30)

class Staff(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    #department = models.CharField(max_length=30)
