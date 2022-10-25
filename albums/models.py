from email.policy import default
from unicodedata import decimal
from django.db import models
from django_extensions.db.models import TimeStampedModel

from artists.models import Artist

# Create your models here.
class Album(TimeStampedModel):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='New Album')
    released_at = models.DateTimeField(null=False)
    cost = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    is_verified = models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']