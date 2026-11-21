from rest_framework import serializers
from app_003_serialization.models import *

#validation method using validators
def validate_name(value):
    if value.lower() == 'ak':
        raise serializers.ValidationError('Name should not be akash')
    return value

class detailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100, validators=[validate_name,])
    info = serializers.CharField(max_length = 100)
    phone = serializers.CharField(max_length = 15)

    #Field level validation
    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Phone number must contain exactly 10 digits.')
        return value

    #Object level validation
    def validate(self, data):
        info = data.get('info', '')
        phone = data.get('phone', '')
        if info.lower() == 'har har mahadev':
            if phone != '8888120866':
                raise serializers.ValidationError('Phone number should be 8888120866 for info har har mahadev')
        return data

    def create(self, validated_data):
        #return super().create(validated_data)
        return detail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #return super().update(instance, validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.info = validated_data.get('info', instance.info)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance