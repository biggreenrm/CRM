# First-party
from .models import Company
from .serializers import CompanySerializer

# Django
from django.shortcuts import render

# Third-party
from rest_framework import viewsets
from rest_framework import permissions


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт, который позволяет компаниям быть отображенными, или изменять их.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated] # как это работает?