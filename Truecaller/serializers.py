from rest_framework import serializers
from . models import Contact


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'mobile', 'email', 'address', 'created_at', 'updated_at')
