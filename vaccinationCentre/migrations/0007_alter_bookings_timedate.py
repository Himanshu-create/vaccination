# Generated by Django 4.0.6 on 2022-07-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinationCentre', '0006_alter_bookings_timedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='timeDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]