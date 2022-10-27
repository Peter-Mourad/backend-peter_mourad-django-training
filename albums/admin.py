from django.contrib import admin

from albums.models import Album, Song

class ShowAlbumsAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'name', 'released_at', 'cost', 'is_verified')

admin.site.register(Album, ShowAlbumsAdmin)
admin.site.register(Song)