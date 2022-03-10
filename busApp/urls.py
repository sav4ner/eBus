# from importlib.resources import path
from django.urls import path
from django.conf.urls import *
from busApp.views import *
from django.contrib import admin

from busApp.models import bookings, category, status, bustype, employee, route, bus


urlpatterns = [
    path('api/v1/bookings',listBookings.as_view(),name='bookings'),
    path('api/v1/bookings/<int:pk>/',detailBookings.as_view() ,name = 'singlebookings'),

    path('api/v1/routes',listRoutes.as_view(), name='destination'),
    path('api/v1/routes/<int:pk>/',detailRoutes.as_view(), name='singleroute'),

    path('api/v1/bus',listBus.as_view(), name='hotel'),
    path('api/v1/bus/<int:pk>/',detailBus.as_view(), name='singlebus'),

    path('api/v1/employee',listEmployee.as_view(), name='bookings'),
    path('api/v1/employee/<int:pk>/',detailEmployee.as_view(), name='singleEmployee'),

    
]
