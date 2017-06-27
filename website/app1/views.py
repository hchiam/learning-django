# from django.shortcuts import render
# 
# # Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is the app1 app homepage!</h1>')

def detail(request, album_id): # example: album_id=712
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

