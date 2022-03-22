from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name  = 'index.html'),
    path('view_all_emp',views.view_all_emp,name  = 'view_all_emp.html'),
    path('view_all_dept',views.view_all_dept,name  = 'view_all_dept.html'),
    path('add_an_emp',views.add_an_emp,name  = 'add_an_emp.html'),
    path('add_dept',views.add_dept ,name  = 'add_dept.html'),
    path('rem_an_emp',views.rem_an_emp,name  = 'rem_an_emp.html'),
    path('rem_an_emp/<int:emp_id>',views.rem_an_emp,name  = 'rem_an_emp.html'),
    path('filt_emp_det',views.filt_emp_det,name  = 'filt_emp_det.html'),
    
]
