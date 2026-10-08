from rest_framework import serializers
from rest_framework.response import Response

from apps.contacts.models import ContactModel
from core.constants.choices import StatusChoices


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('id', 'name', 'email', 'phone', 'company', 'status', 'created_at', 'updated_at')

    @staticmethod
    def validate_phone(value: str):
        if value.startswith('0'):
            value = '+38' + value
        return value

    def create(self, validated_data):
        validated_data['status'] = StatusChoices.NEW
        return super().create(validated_data)

