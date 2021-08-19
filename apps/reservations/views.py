import string, random

from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework import filters
from rest_framework import generics

from .models import Client, Room, Reservation, Invoice
from .serializers import ClientSerializers, RoomSerializers, ReservationSerializers, InvoiceSerializers

class SearchAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        if self.request.query_params['type'] == 'client':
            self.search_fields = ['firstname', 'dni']
            self.serializer_class = ClientSerializers
            queryset = Client.objects.all()
            return queryset

        if self.request.query_params['type'] == 'room':
            self.search_fields = ['name', 'type_room', 'status']
            self.serializer_class = RoomSerializers
            queryset = Room.objects.all()
            return queryset

        if self.request.query_params['type'] == 'reservation':
            self.search_fields = ['date', 'status']
            self.serializer_class = ReservationSerializers
            queryset = Reservation.objects.all()
            return queryset

        if self.request.query_params['type'] == 'invoice':
            self.search_fields = ['code', 'type_payment', 'date']
            self.serializer_class = InvoiceSerializers
            queryset = Invoice.objects.all()
            return queryset

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializers

    def list(self, request):
        clients = Client.objects.filter(deleted=False)
        client_serializers = ClientSerializers(clients, many=True)
        return Response(client_serializers.data, status.HTTP_200_OK)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Client created successfully.', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            client_serializers = self.serializer_class(self.get_queryset(pk), data=request.data)
            if client_serializers.is_valid():
                client_serializers.save()
                return Response({'message': 'Client updated successfully.', 'data': client_serializers.data},
                                status=status.HTTP_200_OK)
        return Response(client_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        client = self.get_queryset().filter(id=pk).first()

        if client:
            client.deleted = True
            client.save()
            return Response({'message': 'Client deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Client not found.'}, status=status.HTTP_400_BAD_REQUEST)


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializers

    def list(self, request):
        rooms = Room.objects.filter(deleted=False)
        room_serializers = RoomSerializers(rooms, many=True)
        return Response(room_serializers.data, status.HTTP_200_OK)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Room created successfully.', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            room_serializers = self.serializer_class(self.get_queryset(pk), data=request.data)
            if room_serializers.is_valid():
                room_serializers.save()
                return Response({'message': 'room update successfully.', 'data': room_serializers.data},
                                status=status.HTTP_200_OK)
        return Response(room_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        room = self.get_queryset().filter(id=pk).first()

        if room:
            room.deleted = True
            room.save()
            return Response({'message': 'room deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Room not found.'}, status=status.HTTP_400_BAD_REQUEST)


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializers

    def list(self, request):
        reservations = Reservation.objects.all()
        reservation_serializers = ReservationSerializers(reservations, many=True)
        return Response(reservation_serializers.data, status.HTTP_200_OK)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'reservation created successfully.', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            reservation_serializers = self.serializer_class(self.get_queryset(pk), data=request.data)
            if reservation_serializers.is_valid():
                reservation_serializers.save()
                return Response({'message': 'room update successfully.', 'data': reservation_serializers.data},
                                status=status.HTTP_200_OK)
        return Response(reservation_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        reservation = self.get_queryset().filter(id=pk).first()

        if reservation:
            reservation.status = 'DELETED'
            reservation.save()
            return Response({'message': 'room deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Room not found.'}, status=status.HTTP_400_BAD_REQUEST)


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializers

    def list(self, request):
        invoices = Invoice.objects.filter(deleted=False)
        invoice_serializers = InvoiceSerializers(invoices, many=True)
        return Response(invoice_serializers.data, status.HTTP_200_OK)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        request.data.update({'code': code})

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            reservation = Reservation.objects.filter(pk=request.data['reservation']).first()
            reservation.status = 'PAID'
            reservation.save()

            return Response({'message': 'reservation created successfully.', 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        invoice = self.get_queryset().filter(id=pk).first()

        if invoice:
            invoice.deleted = True
            invoice.save()
            return Response({'message': 'Invoice deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invoice not found.'}, status=status.HTTP_400_BAD_REQUEST)