from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "position",
                    "company", "sex", "salary", "date_of_birth",
                    "date_of_hiring")
