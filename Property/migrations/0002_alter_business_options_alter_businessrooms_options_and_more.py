# Generated by Django 4.0.2 on 2022-02-12 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name_plural': 'Business Storages'},
        ),
        migrations.AlterModelOptions(
            name='businessrooms',
            options={'verbose_name_plural': 'Rooms for Business Storage'},
        ),
        migrations.AlterModelOptions(
            name='climatecontrolled',
            options={'verbose_name_plural': 'Climate Controlled'},
        ),
        migrations.AlterModelOptions(
            name='garage',
            options={'verbose_name_plural': 'Garages'},
        ),
        migrations.AlterModelOptions(
            name='machinery',
            options={'verbose_name_plural': 'Machinery'},
        ),
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name_plural': 'Personal'},
        ),
        migrations.AlterModelOptions(
            name='propertyfacilities',
            options={'verbose_name_plural': 'Property Facilities'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name_plural': 'Vehicles'},
        ),
    ]
