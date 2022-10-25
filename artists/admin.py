from django.contrib import admin

from .models import Artist
from albums.models import Album

class AlbumsInlineAdmin(admin.TabularInline):
    model = Album

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'social_link', 'num_approved_albums']

    def num_approved_albums(self, artist):
        return artist.album_set.filter(is_verified=True).count()

    inlines=[AlbumsInlineAdmin]

admin.site.register(Artist, ArtistAdmin)