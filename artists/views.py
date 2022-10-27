from django.shortcuts import render
from django.views import View
from .forms import ArtistForm
from .models import Artist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class ArtistsHomePage(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'artists_list.html', {'artists' : artists})


class CreateArtist(LoginRequiredMixin, View):
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


class ArtistLogin(View):
    def get(self, request):
        return render(request, 'login_form.html', {})

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        err = ''
        if user is not None:
            login(request, user)
        else:
            err = 'Invalid username or password'
            print(err)

        return render(request, 'login_form.html', {'error': err})

