from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    summary = models.TextField(blank=True)
    type_of_book = models.CharField(max_length=50)
    readers = models.CharField(max_length=250, blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]