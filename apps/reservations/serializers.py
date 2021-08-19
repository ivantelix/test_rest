from rest_framework import serializers
from rest_framework import status
from .models import Client, Room, Reservation, Invoice

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'client': instance.client.firstname,
            'room': instance.room.name,
            'status': instance.status,
            'date': instance.date,
            'date_end': instance.date_end,
            'days': (instance.date_end - instance.date).days
        }


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"

    def to_representation(self, instance):
        return {
            'code': instance.code,
            'reservation': instance.reservation.client.firstname,
            'amount': instance.amount,
            'type_payment': instance.type_payment,
            'date': instance.date
        }

    def validate(self, attrs):

        reservation = Reservation.objects.filter(pk=attrs['reservation'].id).first()

        if reservation.status == "PAID":
            raise serializers.ValidationError({'message': 'This invoice already has a payment registered.!',
                                                    'status': status.HTTP_400_BAD_REQUEST})

        if reservation.status == "DELETED":
            raise serializers.ValidationError({'message': 'Invoice not found or deleted.!',
                                                    'status': status.HTTP_400_BAD_REQUEST})

        if reservation.room.amount != attrs['amount']:
            raise serializers.ValidationError({'message': 'The amount does not match the amount of the reservation',
                                                    'status': status.HTTP_400_BAD_REQUEST})

        return attrs
