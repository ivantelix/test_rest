# Generated by Django 3.2.6 on 2021-08-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_invoice_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_end',
            field=models.DateField(verbose_name='Date End Reservation'),
        ),
    ]