# First-party
from .models import Employee
from .serializers import EmployeeSerializer

# Django
from django.shortcuts import render

# Third-party
from rest_framework import viewsets
from rest_framework import permissions


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт, который позволяет компаниям быть отображенными, или изменять их.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]