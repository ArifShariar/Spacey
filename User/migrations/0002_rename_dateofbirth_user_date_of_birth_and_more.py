# Generated by Django 4.0.2 on 2022-02-16 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dateOfBirth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nidNumber',
            new_name='nid_number',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
