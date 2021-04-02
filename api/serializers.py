from rest_framework import serializers
from .models import *

class StatesSerializer (serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'

class CitiesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
