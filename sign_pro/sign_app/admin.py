from django.contrib import admin
from .models import Employee,signupdata

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'city']

admin.site.register(Employee)

admin.site.register(signupdata)