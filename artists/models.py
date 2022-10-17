from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artist(models.Model):
    stage_name = models.CharField(primary_key=True, max_length=100, null=False)
    social_link = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.stage_name