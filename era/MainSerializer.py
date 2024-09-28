from rest_framework import serializers
from .models import era



class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = era
        fields = "__all__"