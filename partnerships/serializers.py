# First-party
from .models import Partnership

# Third-party
from rest_framework import serializers


# Serializer для модели Employee
class PartnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partnership
        fields = ['company1', 'company2', 'start_date']