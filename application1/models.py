from django.db import models
class Employees(models.Model):
    
    employeename=models.CharField(max_length=25)
    employeeaddress=models.CharField(max_length=50)
    employeecontactnumber=models.IntegerField(max_length=25)
    employeeemailid=models.EmailField()
    employeeage=models.IntegerField(max_length=20)



