from django.contrib import admin

from albums.models import Album

class ShowAlbumsAdmin(admin.ModelAdmin):
    list_display = ('album_id', 'artist_name', 'name', 'created_at', 'released_at', 'cost', 'is_verified')

class FlatPageAdmin(admin.ModelAdmin):
    fields = ['created_at']

admin.site.register(Album, ShowAlbumsAdmin)