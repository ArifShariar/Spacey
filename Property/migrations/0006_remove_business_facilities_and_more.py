# Generated by Django 4.0.2 on 2022-02-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0005_rename_name_business_property_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='climatecontrolled',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='facilities',
        ),
    ]
