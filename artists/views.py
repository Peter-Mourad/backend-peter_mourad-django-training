from django.shortcuts import render
from django.views import View
from .forms import ArtistForm
from .models import Artist
from django.contrib.auth.mixins import LoginRequiredMixin


class ArtistsHomePage(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'artists_list.html', {'artists' : artists})


class CreateArtist(LoginRequiredMixin, View):
    login_url = '/admin'

    def get(self, request):
        form = ArtistForm()
        return render(request, 'artist_form.html', {'form': form})

    def post(self, request):
        err = ''
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
        else: 
            err = form.errors.as_text()

        context = {'form': ArtistForm, 'error': err}
        return render(request, 'artist_form.html', context)

