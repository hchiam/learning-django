from django.contrib import admin

# Register your models here.

from .models import Album, Song

admin.site.register(Album) # --> http://127.0.0.1:8000/admin/ should now show an App1 section with Albums in it
admin.site.register(Song)
