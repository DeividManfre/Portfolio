from rest_framework import viewsets
from cars.serializer import CarSerializer, ColorSerializer
from cars.models import Car, Color


class CarViewSet(viewsets.ModelViewSet):
    """View all car's"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ColorViewSet(viewsets.ModelViewSet):
    """View all color's"""
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
