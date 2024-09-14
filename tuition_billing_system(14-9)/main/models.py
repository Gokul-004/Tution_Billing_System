from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subjects_available = models.ManyToManyField('Subject')
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    subjects = models.ManyToManyField(Subject)

    def total_fees(self):
        return sum(subject.fee for subject in self.subjects.all())

    def __str__(self):
        return self.name
