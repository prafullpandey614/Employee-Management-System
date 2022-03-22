from django.contrib import admin
from .models import Employee,Department,role
admin.site.register(Employee)
admin.site.register(role)
admin.site.register(Department)
# Register your models here.
