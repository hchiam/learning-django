# from django.http import HttpResponse
# from django.template import loader # to load separate template files
from django.shortcuts import render # instead of using loader or HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404 # instead of using Http404
from .models import Album, Song


def index(request):
    # html = '<h1>This is the app1 app homepage!</h1>'
    # all_albums = Album.objects.all()
    # for album in all_albums:
    #     url = '/app1/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br/>'
    # return HttpResponse(html)
    
    # |
    # |
    # V
    
    # all_albums = Album.objects.all() # get database data
    # template = loader.get_template('app1/index.html') # by default django looks into local /templates/ folder
    # context = {'all_albums': all_albums}
    # return HttpResponse(template.render(context, request))
    
    # |
    # |
    # V
    
    all_albums = Album.objects.all() # get database data
    template = 'app1/index.html'
    template_info = {'all_albums': all_albums} # aka context
    return render(request, template, template_info)


def detail(request, album_id): # example: album_id=712
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
    
    # |
    # |
    # V
    
    # # responding depending on if request gets a valid entry
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404('Album does not exist. :(')
    
    # |
    # |
    # V
    
    album = get_object_or_404(Album, pk=album_id) # to replace that try/except statement
    
    template = 'app1/detail.html'
    template_info = {'album': album} # aka context
    return render(request, template, template_info)


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    
    # account for unselected id:
    try:
        selected_song = album.song_set.get(pk=request.POST['song']) # request.POST['song'] means get id of the song that was selected
    except (KeyError, Song.DoesNotExist):
        # redirect to same template details page but also give error_message
        template = 'app1/detail.html'
        template_info = { # aka context
            'album': album,
            'error_message': 'You did not select a valid song.',
        }
        return render(request, template, template_info)
    else:
        # update database, just like we did with the CLI shell:
        selected_song.is_favourite = True
        selected_song.save()
        # return response
        template = 'app1/detail.html'
        template_info = {'album': album} # aka context
        return render(request, template, template_info)



























