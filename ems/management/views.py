from django.shortcuts import render

from .models import Employee,Department,Timesheet,Salary
def home_page(request):
    return render(request,'home_page.html')

def get_all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def get_all_departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})