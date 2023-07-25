
from django.contrib import admin
from django.urls import path

from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home_page'),
    path('home/',views.home_page,name='home_page'),

]
