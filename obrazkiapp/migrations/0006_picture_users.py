# Generated by Django 4.2.11 on 2024-03-28 07:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obrazkiapp', '0005_remove_picture_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]