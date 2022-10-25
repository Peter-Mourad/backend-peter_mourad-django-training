from django.shortcuts import render
from .forms import AlbumForm

def CreateAlbum(request):
    form = AlbumForm
    err = ''
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = form.errors.as_text()
            print(err)
            
    context = {'form': AlbumForm, 'error': err}
    return render(request, 'album_form.html', context)