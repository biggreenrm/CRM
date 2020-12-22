# First-party
from .models import Partnership
from .serializers import PartnershipSerializer

# Django
from django.shortcuts import render

# Third-party
from rest_framework import viewsets
from rest_framework import permissions


class PartnershipViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт, который позволяет партнёрствам быть отображенными или изменёнными.
    """
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer
    permission_classes = [permissions.IsAuthenticated]