from rest_framework import serializers

from .models import Cafes


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafes
        fields = '__all__'
