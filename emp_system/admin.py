from django.contrib import admin
from .models import Department,Employee,Role
# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)


