
from django.contrib import admin
from django.urls import path

from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home_page'),
    path('home/',views.home_page,name='home_page'),
    path('employees/',views.get_all_employees,name='employees'),
    path('departments/',views.get_all_departments,name='departments'),
    path('department/add',views.add_department,name='add_dep'),
    path('department/edit/<int:dep_id>/',views.update_department,name='update_dep'),
    path('department/delete/<int:dep_id>/',views.delete_department,name='update_dep'),
    path('employee/add/',views.add_employee,name='add_employee'),
    path('employee/edit/<int:emp_id>/', views.update_employee, name='edit_employee'),
    path('employee/delete/<int:emp_id>/', views.delete_employee, name='edit_employee'),
    path('employee/<int:emp_id>/timesheets/', views.get_all_timesheets, name='employee_timesheets'),

    path('employee/<int:emp_id>/add/timesheet/', views.add_timesheet, name='add_new_timesheet'),
    path('employee/<int:emp_id>/add/salary/', views.add_salary, name='add_new_salary'),
    path('employee/<int:emp_id>/salaries/', views.get_all_salaries, name='employee_salaries'),

    path('employee/<int:emp_id>/',views.delete_employee,name='del_emp'),
    path('department/<int:dep_id>/',views.delete_department,name='del_dep'),

]
