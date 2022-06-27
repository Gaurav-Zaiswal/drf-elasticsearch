from dataclasses import fields
from rest_framework import serializers

from .models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classroom
        fields = ['class_name', 'class_description']

