# Generated by Django 4.2.11 on 2024-03-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrazkiapp', '0003_rename_size_picture_height_picture_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rectangle',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rectangle',
            name='y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='picture',
            name='color',
            field=models.CharField(default='red', max_length=30),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(default='New Picture', max_length=200, unique=True),
        ),
    ]
