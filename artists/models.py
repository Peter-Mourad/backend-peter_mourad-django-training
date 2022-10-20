from django.db import models
from django.db.models import Q, Count

class ArtistQuerySet(models.QuerySet):
    def annotated(self):
        return self.annotate(approved_albums=Count('album', filter=Q(is_verified=True)))

class ArtistManager(models.Manager):
    def annotated(self):
        return self.ArtistQuerySet(self.model, using=self._db).annotated()

class Artist(models.Model):
    stage_name = models.CharField(primary_key=True, max_length=100, null=False)
    social_link = models.CharField(null=False, max_length=100)
    objects=ArtistManager()

    def __str__(self):
        return self.stage_name