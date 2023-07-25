from django.shortcuts import render,redirect,get_object_or_404

from .models import Employee,Department,Timesheet,Salary
def home_page(request):
    return render(request,'home_page.html')

def get_all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def get_all_departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})


def get_all_timesheets(request,emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    timesheets = Timesheet.objects.select_related('employee').filter(employee=employee)  # Use select_related to reduce DB hits when referencing foreign key
    context = {
        'timesheets': timesheets
    }
    return render(request, 'employee_timesheets.html', context)


def get_all_salaries(request,emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    salaries = Salary.objects.select_related('employee').filter(employee=employee)   # Use select_related to reduce DB hits when referencing foreign key
    context = {
        'salaries': salaries
    }
    return render(request, 'employee_salaries.html', context)

def delete_employee(request,emp_id):
    Employee.objects.filter(pk=emp_id).delete()
    return redirect('employees')

def delete_department(request,dep_id):
    Department.objects.filter(pk=dep_id).delete()
    return redirect('departments')



from .forms import DepartmentForm


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            Department.objects.create(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
            )
            return redirect('departments')
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})


from .forms import EmployeeForm
from django.contrib.auth.hashers import make_password
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Get the validated form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            position = form.cleaned_data['position']
            department = form.cleaned_data['department']

            # Create the employee
            employee = Employee(
                username=username,
                password=make_password(password),  # Hash the password
                first_name=first_name,
                last_name=last_name,
                mobile_number=mobile_number,
                email=email,
                position=position,
                department=department,
            )
            employee.save()

            return redirect('employees')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})




def update_department(request, dep_id):
    department = get_object_or_404(Department, department_id=dep_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            location = form.cleaned_data["location"]
            department.name = name
            department.location = location
            department.save()
            return redirect('departments') # redirect to the page where you display all departments
    else:
        form = DepartmentForm()
        form.fields['name'].initial = department.name
        form.fields['location'].initial = department.location
    return render(request, 'update_department.html', {'form': form, 'department': department})

