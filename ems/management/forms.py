from django import forms
from .models import Department,Employee
class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=256, required=True)
    location = forms.CharField(max_length=100, required=True)

class EmployeeForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    mobile_number = forms.CharField(max_length=12, required=True)
    email = forms.EmailField(max_length=254, required=True)
    position = forms.CharField(max_length=126, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    department = forms.ModelChoiceField(queryset=Department.objects.only("name").all())

class TimesheetForm(forms.Form):
    date = forms.DateField(required=True)
    hours_worked = forms.FloatField(required=True)

class SalaryForm(forms.Form):
    monthly_salary = forms.FloatField()