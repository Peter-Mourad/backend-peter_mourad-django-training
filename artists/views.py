from contextlib import nullcontext
from django.shortcuts import render
from .forms import ArtistForm
from .models import Artist


def ArtistsHomePage(request):
    artists = Artist.objects.all()
    return render(request, 'artists_list.html', {'artists' : artists})


def CreateArtist(request):
    form = ArtistForm
    err = ''
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
        else: 
            err = form.errors.as_text()

    context = {'form': ArtistForm, 'error': err}
    return render(request, 'artist_form.html', context)