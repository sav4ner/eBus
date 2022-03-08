# from importlib.resources import path
from django.urls import path
from django.conf.urls import *
from busApp.views import *
from django.contrib import admin

from busApp.models import bookings, category, status, bustype, employee, route, bus


urlpatterns = [
    url(r'^api/v1/bookings$',listBookings.as_view(),name='bookings'),
    url(r'^api/v1/bookings/(?P<id>\d+)$',detailBookings.as_view() ,name = 'singleuser'),

    url(r'^api/v1/routes$',listRoutes.as_view(), name='destination'),
    url(r'api/v1/routes/(?P<id>\d+)$',detailRoutes.as_view(), name='singledestination'),

    url(r'api/v1/bus$',listBus.as_view(), name='hotel'),
    url(r'^api/v1/bus/(?P<id>\d+)$',detailBus.as_view(), name='singlehotel'),

    url(r'^api/v1/employee$',listEmployee.as_view(), name='bookings'),
    url(r'^api/v1/employee/(?P<id>\d+)$',detailEmployee.as_view(), name='singlebooking'),

    
]
