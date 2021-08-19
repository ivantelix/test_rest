from django.db import models

class Client(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="First Name", blank=False, null=False)
    lastname = models.CharField(max_length=50, verbose_name="Last Name", blank=True, null=True)
    dni = models.CharField(max_length=20, verbose_name="DNI", unique=True, blank=False, null=False)
    address = models.TextField(max_length=150, verbose_name="Address", blank=True, null=True, default="")
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class Room(models.Model):
    CHOICE_TYPE = (
        ('SIMPLE', 'Simple'),
        ('DOUBLE', 'DoUble'),
        ('TRIPLE', 'Triple'),
        ('FAMILY', 'Family')
    )

    CHOICE_STATUS = (
        ('FREE', 'Free'),
        ('OCCUPIED', 'Occupied')
    )

    name = models.CharField(max_length=50, verbose_name="Name", blank=False, null=False)
    description = models.CharField(max_length=150, verbose_name="Description", blank=True, null=True, default="")
    type_room = models.CharField(max_length=15, choices=CHOICE_TYPE, default=1, verbose_name="Type Room",
                                 blank=False, null=False)
    num_beds = models.IntegerField(default=1, verbose_name="Number of Beds", blank=False, null=False)
    amount = models.FloatField(default=0.00, verbose_name="Amount", blank=False, null=False)
    status = models.CharField(max_length=15, choices=CHOICE_STATUS, blank=False, null=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


    def __str__(self):
        return self.name


class Reservation(models.Model):
    CHOICE_RESERVATION = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('DELETED', 'Deleted')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False, null=False)
    status = models.CharField(max_length=15, choices=CHOICE_RESERVATION, default="PENDING", blank=False, null=False)
    date = models.DateField(verbose_name="Date Reservation", auto_now=True)
    date_end = models.DateField(verbose_name="Date End Reservation", blank=False, null=False)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return '{} {}'.format(self.client.firstname, self.client.lastname)


class Invoice(models.Model):
    CHOICE_TYPE_PAYMENT = (
        ('CC', 'Credit Card'),
        ('CASH', 'Cash')
    )

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=False, null=False)
    code = models.CharField(max_length=10, unique=True, verbose_name="Code")
    amount = models.FloatField(default=0.00, verbose_name="Amount", blank=False, null=False)
    type_payment = models.CharField(max_length=15, choices=CHOICE_TYPE_PAYMENT, blank=False, null=False)
    date = models.DateField(verbose_name="Date Payment", auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return '{}'.format(self.code)