from tkinter import CASCADE
from django.db import models

# Create your models here.
class person(models.Model):
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=15)
  age = models.PositiveIntegerField()
  email = models.EmailField()
  dob = models.DateField()
  is_married = models.BooleanField(default=False)
  
  def __str__(self):
    return self.first_name
  
class citizenship(models.Model):
  citizenship_no = models.IntegerField()
  person = models.OneToOneField(person, on_delete = models.CASCADE)
  
def __str__(self):
    return self.person
  
  
class children(models.Model):
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=15)
  age = models.IntegerField()
  parents = models.ForeignKey(person, on_delete= models.SET_NULL, null= True)

def __str__(self):
    return self.first_name
