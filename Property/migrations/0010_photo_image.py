# Generated by Django 4.0.2 on 2022-02-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0009_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=0, null=True, upload_to=''),
        ),
    ]
