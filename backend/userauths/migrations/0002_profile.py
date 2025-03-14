# Generated by Django 4.2.7 on 2025-03-14 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default_user.png', null=True, upload_to='user_folder')),
                ('full_name', models.CharField(max_length=200)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
