from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField


from artists.models import Artist

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


class Song(models.Model):
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=album_name)
    image = models.ImageField(upload_to='./media/images', blank=False, null=False)
    image_thumbnail = ImageSpecField(source='image', format='jpeg')
    audio = models.FileField(upload_to='./media/audio', validators=[FileExtensionValidator(["mp3", 'wav'])], blank=False, null=False)
