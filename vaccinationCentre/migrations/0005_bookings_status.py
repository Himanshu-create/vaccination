# Generated by Django 4.0.6 on 2022-07-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinationCentre', '0004_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='status',
            field=models.CharField(default='Not Vaccinated', max_length=40, null=True, verbose_name='Status'),
        ),
    ]