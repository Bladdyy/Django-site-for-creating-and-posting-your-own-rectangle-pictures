from datetime import timezone
from django.utils.timezone import now
from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100, default="New Tag")

    def __str__(self):
        return "Tag name: " + str(self.name)


class Picture(models.Model):
    name = models.CharField(unique=True, max_length=200, default="New Picture")
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=100)
    users = models.ManyToManyField(get_user_model())
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return ("Picture name: " + str(self.name)
                + "\nwidth: " + str(self.width)
                + "\nheight: " + str(self.height))


class Rectangle(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    height = models.FloatField(default=5)
    width = models.FloatField(default=5)
    color = models.CharField(max_length=30, default="red")
    picture = models.ForeignKey(Picture, related_name='rectangles', on_delete=models.CASCADE)

    def __str__(self):
        return ("Rectangle color: " + str(self.color)
                + "\nheight: " + str(self.height)
                + "\n width: " + str(self.width)
                + "\nx coordinates: " + str(self.x)
                + "\ny coordinates:" + str(self.y))
