# First-party
from .models import Employee

# Third-party
from rest_framework import serializers


# Serializer для модели Employee
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'second_name', 'position', 'company', 'sex', 'salary', 'date_of_birth', 'date_of_hiring']