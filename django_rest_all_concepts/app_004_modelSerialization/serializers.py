from rest_framework import serializers
from app_004_modelSerialization.models import *


#validation method using validators
def validate_name(value):
    if value.lower() == 'ak':
        raise serializers.ValidationError('Name should not be akash')
    return value

class informationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])
    class Meta:
        model = information
        fields = '__all__'