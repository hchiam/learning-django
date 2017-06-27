# from django.shortcuts import render
# 
# # Create your views here.

from django.http import HttpResponse
from django.template import loader # to load separate template files
from .models import Album


def index(request):
    # html = '<h1>This is the app1 app homepage!</h1>'
    # all_albums = Album.objects.all()
    # for album in all_albums:
    #     url = '/app1/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br/>'
    # return HttpResponse(html)
    all_albums = Album.objects.all() # get database data
    template = loader.get_template('app1/index.html') # by default django looks into local /templates/ folder
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id): # example: album_id=712
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

