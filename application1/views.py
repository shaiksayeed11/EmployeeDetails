from django.shortcuts import render
from application1.models import Employees
def f1(request):
    data=Employees.objects.all()
    return render(request,"application1/index.html",{"data":data})



