from django.contrib import admin
from .models import Client, Room, Reservation, Invoice

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'dni']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type_room', 'amount', 'status']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'status', 'client', 'room']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'reservation', 'amount', 'type_payment', 'date', 'deleted']

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Invoice, InvoiceAdmin)
