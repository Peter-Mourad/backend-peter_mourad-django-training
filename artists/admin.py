from django.contrib import admin
from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'social_link', 'num_approved_albums']

    def num_approved_albums(self, artist):
        return artist.album_set.filter(is_verified=True).count()

admin.site.register(Artist, ArtistAdmin)