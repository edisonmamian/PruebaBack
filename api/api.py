from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

class StateApi(APIView):
    def post (self, request):
        serializer = StatesSerializer (data = request.data)
        if serializer.is_valid():
            state = serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
