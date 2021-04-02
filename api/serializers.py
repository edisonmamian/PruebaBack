from rest_framework import serializers

class StatesSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.CharField()

    def create (self, validate_data):
        pass

class CitiesSerializer (serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.CharField()
    zip = serializers.CharField()
