# First-party
from .models import Company

# Third-party
from rest_framework import serializers

# Serializer для модели Company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'country', 'foundation', 'area']