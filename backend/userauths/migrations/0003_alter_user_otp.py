# Generated by Django 4.2.7 on 2025-03-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
