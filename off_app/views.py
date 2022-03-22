from datetime import datetime
from hmac import new
from multiprocessing import context
from os import name
from django.shortcuts import render ,HttpResponse
from pyrsistent import v
from telegram import Location
from .models import Employee,role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')
def add_dept(request):
    if request.method=="POST":
        dept_name = request.POST['dept_name']
        dept_loct = request.POST['loct_name']
        new_dept = Department(name = dept_name, location = dept_loct )
        new_dept.save()
        return HttpResponse('Department Added Succesfully')
    elif request.method == "GET":
        return render(request,'add_dept.html')
    else :
        return HttpResponse('An Exception Occured')
    
def add_an_emp(request):
    if(request.method=="POST"):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name = first_name , last_name=last_name,dept_id = dept,role_id = role,bonus=bonus,salary =salary,phone= phone,hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Succesfully')
    elif request.method == "GET":
        return render(request,'add_an_emp.html')
    else :
        return HttpResponse("Some Exception Occured. Employee Cannot Saved")
def rem_an_emp(request,emp_id = 0):
    if emp_id:
        try:
            empl_to_b_rem = Employee.objects.get(id = emp_id)
            empl_to_b_rem.delete()
            return HttpResponse("Employee Removed Succesfully")
        except:
            return HttpResponse("Employee Id Not Found")
        
    emps =Employee.objects.all()
    context = {
        "emps":emps
    }
    
    return render(request,'rem_an_emp.html',context)
def view_all_emp(request):
    emps = Employee.objects.all()
    context = {
       "emps" : emps
    }
    
    return render(request,'view_all_emp.html',context)
def view_all_dept(request):
    depts = Department.objects.all()
    context = {
       "depts" : depts
    }
    
    return render(request,'view_all_dept.html',context)
def filt_emp_det(request):
    if request.method=="POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        
        if name:
            emps =emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name) )
        if dept:
            emps = emps.filter(Q(dept__name__icontains=name))
        if role:
            emps = emps.filter(Q(role__name__icontains=name))
        context = {
            "emps":emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method=="GET":
        return render(request,'filt_emp_det.html')
            
        
    else:
        return HttpResponse("Something Went Wrong..!")
                
    