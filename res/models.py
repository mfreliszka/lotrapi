from django.db import models

class DateModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)

    edited = models.DateTimeField(auto_now=True)


class World(DateModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

class Character(DateModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    height = models.CharField(max_length=10, blank=True)

    gender = models.CharField(max_length=40, blank=True)

class Film(DateModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    characters = models.ManyToManyField(
        Character,
        related_name="films",
        blank=True
    )

    worlds = models.ManyToManyField(
        World,
        related_name="films",
        blank=True
    )
