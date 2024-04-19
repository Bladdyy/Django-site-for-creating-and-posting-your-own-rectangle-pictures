import random
import string

from django.core.management.base import BaseCommand

from obrazkiapp.models import Picture, Tag, Rectangle


class Command(BaseCommand):
    help = 'Creates random pictures made of rectangles.'

    def add_arguments(self, parser):
        parser.add_argument('number', nargs='?', type=int, default=5)

    def handle(self, *args, **options):
        num = options['number']
        hex = ['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(num):
            height = random.randint(100, 600)
            width = random.randint(100, 600)
            tags = list(Tag.objects.get_queryset())
            tags = random.sample(tags, random.randint(1, len(tags)))
            pict = Picture(name=''.join(random.choice(string.ascii_lowercase) for i in range(10)),
                           height=height,
                           width=width,
                           )
            pict.save()
            for tag in tags:
                pict.tags.add(tag.id)
            for i in range(random.randint(10, 35)):
                rect_height = random.randint(10, height)
                rect_width = random.randint(10, width)
                color = "#"
                for i in range(6):
                    color += random.choice(hex)
                rect = Rectangle(x=random.randint(0, height - rect_height),
                          y=random.randint(0, width - rect_width),
                          width=rect_width,
                          height=rect_height,
                          color=color,
                          picture=pict)
                rect.save()
