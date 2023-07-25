from django.db import models

from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)


class Employee(AbstractUser):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    position = models.CharField(max_length=126)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

