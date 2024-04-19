# Generated by Django 4.2.11 on 2024-04-18 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('obrazkiapp', '0006_picture_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Tag', max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(to='obrazkiapp.tag'),
        ),
    ]
