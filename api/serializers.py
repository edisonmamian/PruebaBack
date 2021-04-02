from rest_framework import serializers
from .models import *

class StatesSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.CharField()

    def create (self, validate_data):
        instance = States()
        instance.slug = validate_data.get('slug')
        instance.save()
        return instance

    def validate_slug(self, data):
        states = States.objects.filter(slug = data)
        if len(states) != 0:
            raise serializers.ValidationError("This state already exits")
        else:
            return data

class CitiesSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.CharField()
    zip = serializers.CharField()
