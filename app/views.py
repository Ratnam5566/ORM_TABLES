from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_Dept(request):
    name=input('Enter Name: ')
    no=int(input('Enter Deptno: '))
    l=input('Enter location: ')
    DO=Dept.objects.get_or_create(Dname=name,Deptno=no,Loc=l)[0]
    DO.save()
    return HttpResponse('Data Is Inserted')

def insert_Emp(request):
    Dno=int(input('Enter DeptNumber: '))
    DO=Dept.objects.get_or_create(Deptno=Dno)[0]
    DO.save()
    num=int(input('Enter EmpNumber: '))
    n=input('Enter Ename: ')
    EO=Emp.objects.get_or_create(Eno=num,Ename=n,Deptno=DO)[0]
    return HttpResponse('Data is Updated')

def dispaly_dept(request):
    De=Dept.objects.all()
    D={'De':De}
    return render(request,'dispaly_dept.html',D)


def dispaly_emp(request):
    EO=Emp.objects.all()
    d={'EO':EO}
    return render(request,'dispaly_emp.html',d)