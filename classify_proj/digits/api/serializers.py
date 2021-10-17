from django.db.models import fields
from rest_framework import serializers
from ..models import Digit


class DigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digit
        fields = ("id", "image", "result")
