# Generated by Django 4.2.11 on 2024-04-18 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obrazkiapp', '0007_tag_picture_date_picture_description_picture_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rectangle',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rectangles', to='obrazkiapp.picture'),
        ),
    ]