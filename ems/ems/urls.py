
from django.contrib import admin
from django.urls import path

from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home_page'),
    path('home/',views.home_page,name='home_page'),
    path('employees/',views.get_all_employees,name='employees'),
    path('departments/',views.get_all_departments,name='departments'),

    path('employee/<int:emp_id>/timesheets/', views.get_all_timesheets, name='employee_timesheets'),
    path('employee/<int:emp_id>/salaries/', views.get_all_salaries, name='employee_salaries'),

]
