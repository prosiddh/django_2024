from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField()
    # image=models.ImageField()
    # file=models.FileField()

class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)