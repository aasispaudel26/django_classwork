from django.db import models

# Create your models here.
class person(models.Model):
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=15)
  age = models.PositiveIntegerField()
  email = models.EmailField()
  dob = models.DateField()
  is_married = models.BooleanField(default=False)
