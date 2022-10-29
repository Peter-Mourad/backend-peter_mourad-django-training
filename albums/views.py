from django.shortcuts import render
from .forms import AlbumForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateAlbum(LoginRequiredMixin, View):
    login_url = '/admin'
    
    def get(self, request):
        form = AlbumForm()
        return render(request, 'album_form.html', {'form': form})

    def post(self, request):
        err = ''
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = form.errors.as_text()
                
        context = {'form': AlbumForm, 'error': err}
        return render(request, 'album_form.html', context)