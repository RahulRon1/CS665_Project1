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
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class Timesheet(models.Model):
    timesheet_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(default=0.0)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)


class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)

