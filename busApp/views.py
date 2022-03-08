from operator import ge
from django.shortcuts import render

from inspect import formatannotationrelativeto
from django.shortcuts import render
from rest_framework import generics
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from busApp.models import bookings, employee, route, bus


from busApp.serializers import bookingsSerializer,busSerializer,routeSerializer,employeeSerializer

class detailRoutes (generics.RetrieveUpdateDestroyAPIView):
    queryset = route.objects.all()
    serializer_class = routeSerializer

class listRoutes (generics.ListCreateAPIView):
    queryset = route.objects.all()
    serializer_class = routeSerializer

class detailEmployee (generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class listEmployee (generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class detailBookings (generics.RetrieveUpdateDestroyAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingsSerializer

class listBookings (generics.ListCreateAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingsSerializer

class detailBus (generics.RetrieveUpdateDestroyAPIView):
    queryset = bus.objects.all()
    serializer_class = busSerializer

class listBus (generics.ListCreateAPIView):
    queryset = bus.objects.all()
    serializer_class = busSerializer