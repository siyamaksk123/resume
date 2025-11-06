from rest_framework import serializers
from.models import InformationsModel

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationsModel
        fields = '__all__'