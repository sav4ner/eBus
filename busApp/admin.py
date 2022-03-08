from django.contrib import admin
from busApp.models import bookings, category, status, bustype, employee, route, bus
# Register your models here.
admin.site.register(bookings)
admin.site.register(category)
admin.site.register(status)
admin.site.register(bustype)
admin.site.register(employee)
admin.site.register(bus)
admin.site.register(route)