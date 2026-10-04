from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from .serializers import CarSerializer


class CarAPIView(APIView):

    def get(self, request):
        cached_data = cache.get('cache_key')

        if cached_data is not None:
            return Response(cached_data)

        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)

        cache.set('cache_key', serializer.data, timeout=60)

        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            cache.delete('cache_key')

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

