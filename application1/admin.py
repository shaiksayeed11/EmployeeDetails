from django.contrib import admin
from application1.models import Employees
class EmployeesAdmin(admin.ModelAdmin):
    list_display=["employeename","employeeaddress","employeecontactnumber","employeeemailid","employeeage"]
admin.site.register(Employees,EmployeesAdmin)
