from inspect import formatannotationrelativeto
from django.db.models import fields
from rest_framework import serializers

from busApp.models import bookings, category, status, bustype, employee, route, bus

class routeSerializer (serializers.ModelSerializer):
    class Meta:
        model= route
        fields = (
            'routeId',
            'route',
            'fee',
            'status',

        )

class employeeSerializer (serializers.ModelSerializer):
    class Meta:
        model= employee
        fields = (
            'userteId',
            'firstname',
            'lastname',
            'languages',
            'photo',
            'email',
            'jobtype',
            'contact',
            'status',
        )
class busSerializer (serializers.ModelSerializer):
    class Meta:
        model= bus
        fields = (
            'busId',
            'platenumber',
            'route',
            'bustype',
            'seats',
            'driver',
            'status',
            'ratings'
            
            
        )
class bookingsSerializer (serializers.ModelSerializer):
    class Meta:
        model= bookings
        fields = (
            'bookingId',
            'name',
            'user',
            'email',
            'contact',
            'date',
            'time',
            'fro',
            'destination',
            'bill'
            
        )

