# Generated by Django 3.2.6 on 2021-08-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='code',
            field=models.CharField(max_length=8, unique=True, verbose_name='Code'),
        ),
    ]
