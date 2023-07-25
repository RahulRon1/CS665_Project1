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
        'timesheets': timesheets,
        'employee':employee
    }
    return render(request, 'employee_timesheets.html', context)


def get_all_salaries(request,emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    salaries = Salary.objects.select_related('employee').filter(employee=employee)   # Use select_related to reduce DB hits when referencing foreign key
    context = {
        'salaries': salaries,
        'employee':employee
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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, employee_id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            position = form.cleaned_data["position"]
            department_id = form.cleaned_data["department"]
            mobile_number = form.cleaned_data["mobile_number"]
            employee.username = username
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.position = position
            employee.department_id = department_id
            employee.mobile_number = mobile_number
            employee.save()
            return redirect('employees') # redirect to the page where you display all employees
    else:
        form = EmployeeForm()
        form.fields['username'].initial = employee.username
        form.fields['first_name'].initial = employee.first_name
        form.fields['last_name'].initial = employee.last_name
        form.fields['email'].initial = employee.email
        form.fields['position'].initial = employee.position
        form.fields['department'].initial = employee.department.department_id
        form.fields['mobile_number'].initial = employee.mobile_number
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})

from .forms import TimesheetForm

def add_timesheet(request,emp_id):
    employee = get_object_or_404(Employee, employee_id=emp_id)
    if request.method == 'POST':
        form = TimesheetForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            hours_worked = form.cleaned_data['hours_worked']
            Timesheet.objects.create(date=date, hours_worked=hours_worked, employee=employee)
            return redirect('employee_timesheets', emp_id=employee.employee_id)
    else:
        form = TimesheetForm()

    return render(request, 'add_timesheet.html', {'form': form,'employee':employee})

from .forms import SalaryForm
def add_salary(request,emp_id):
    employee = get_object_or_404(Employee, employee_id=emp_id)
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            monthly_salary = form.cleaned_data['monthly_salary']
            Salary.objects.create(monthly_salary=monthly_salary,employee=employee)
            return redirect('employee_salaries', emp_id=employee.employee_id)
    else:
        form = SalaryForm()

    return render(request, 'add_salary.html', {'form': form,'employee':employee})