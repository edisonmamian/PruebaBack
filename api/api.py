from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET', 'POST'])
def state_api (request):
    if request.method == 'GET':
        states = States.objects.all()
        states_serializer = StatesSerializer (states, many=True)
        return Response(states_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        states_serializer = StatesSerializer (data = request.data)
        if states_serializer.is_valid():
            states_serializer.save()
            return Response({'message': 'State created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(states_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stateDetail_api (request, pk=None):
    state = States.objects.filter(id = pk).first()

    if state:

        if request.method == 'GET':
            states_serializer = StatesSerializer(state)
            return Response(states_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            states_serializer = StatesSerializer(state, data = request.data)
            if states_serializer.is_valid():
                states_serializer.save()
                return Response ({'message': 'State updated'}, status=status.HTTP_200_OK)
            else:
                return Response (states_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            state.delete()
            return Response({'message': 'State deleted'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'State not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def city_api (request):
    if request.method == 'GET':
        cities = Cities.objects.all()
        cities_serializer = CitiesSerializer (cities, many = True)
        return Response(cities_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        cities_serializer = CitiesSerializer(data = request.data)
        if cities_serializer.is_valid():
            cities_serializer.save()
            return Response({'message': 'City created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(cities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cityDetail_api (request, pk=None):
    city = Cities.objects.filter(id=pk).first()

    if city:
        if request.method == 'GET':
            cities_serializer = StatesSerializer(city)
            return Response(cities_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            cities_serializer = StatesSerializer(city, data = request.data)
            if cities_serializer.is_valid():
                cities_serializer.save()
                return Response ({'message': 'City updated'}, status=status.HTTP_200_OK)
            else:
                return Response (cities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            city.delete()
            return Response({'message': 'City deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)
