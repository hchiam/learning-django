# learning-django
Learning Django from [YouTube](https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)

My older repo: https://github.com/hchiam/djangoApp

What's next are my notes from following [thenewboston's YouTube tutorial series](https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK):

# create project "website"
* `django-admin startproject website` (generates the base required files for any django project)
* (Note to self: to remember what files do, read names as if reading directory paths.)
* (Note to self: we're usually going to use website/settings.py and website/urls.py)
* Navigate to website folder so that you see manage.py and website folder.
* `python manage.py runserver`
  * You might have to do something like this beforehand: `export PYTHONPATH=/usr/local/lib/python3.6/site-packages`
  * To make it permanent (i.e. not have to type that every time), add `export PYTHONPATH=/usr/local/lib/python3.6/site-packages` to your .bash_profile file (`open ~/.bash_profile`).
* http://127.0.0.1:8000/
* Hit Ctrl+c to stop the server.

# create "app"
* (Note to self: "apps" are like subdirectories in a URL, like different tabs.)
* (Note to self: each "app" should have a one-liner of what it does.)
* `python manage.py startapp app1`
* (Note: migrations folder is for connecting website to database.)
* (Note: admin.py has admin functionality built in.)
* (Note: apps.py is basically app settings.)
* (Note: models.py is app database model setup.)
* (Note: views.py are basically python functions for requests/responses.)
* Create a urls.py file inside app1.
* Make website/urls.py include app1/urls.py.
* Make app1/urls.py identify a request in the URL and call a function in app1/views.py.
* Make a corresponding response function (in app1/views.py) to the request.
* http://127.0.0.1:8000/app1
* (Note to self: website/website/urls.py --> urlpatterns --> app1/urls.py --> views.py function request response)

# connect/synchronize database
* (Note: db.sqlite3 was automagically created as a default database for testing. Can change to MyQSL later.)
* `python manage.py migrate` (to synchronize code with database)
  * website/settings.py INSTALLED_APPS --> checks app directories for required tables

# create & activate models (how you want to store your data; tables and columns)
* (Note: in Django, python class variables get converted to database columns.)
* Create a class ("table") and variables ("columns") in app1/models.py, while specifying data types.
* Make website/settings.py INSTALLED_APPS include app1/apps.py App1Config() as `'app1.apps.App1Config'`.
* Remember to synchronize database with models! `python manage.py makemigrations app1`.
* (Optional to see what the migration does:)
  * (Migration = change to database.)
  * (`python manage.py sqlmigrate app1 0001` shows changes that converts the model into an SQL file.)
  * (Note the "0001_initial.py".)
* `python manage.py migrate` (so databased synched with code)
* `python manage.py runserver`
* (Note to self: website/website/settings.py INSTALLED_APPS --> models.py --> check classes, variables to synch database)

Remember 3 steps when you want to udpate changes to databases:
1. change website/models.py
2. `python manage.py makemigrations app1`
3. `python manage.py migrate`

# database API
* `python manage.py shell` (and now you can write database commands!)
* Then try these commands, one-by-one:

```
from app1.models import Album, Song
Album.objects.all()
a = Album(artist="the new boston", album_title="Red", genre="Country", album_logo="https://thenewboston.com/photos/users/2/original/e1ee187e9e0225ba124ba1c7c9dbfa56.png")
a.save()
a.artist
a.album_title
a.id # this is the same
a.pk # as this
b = Album()
b.artist = "artist2"
b.album_title = 'title2'
b.genre = 'Jazz'
b.album_logo = 'https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png'
b.save()
a.artist
b.artist
b.album_title = "High School"
b.album_title
exit()
```

# filtering database results (video #10)

## first, set up so filtered results show basic info

* Make app1/models.py Album class to have a `__str__()` function to customize the shell output representation of an Album.
* `python manage.py shell`
* `from app1.models import Album, Song`
* `Album.objects.all()` should output a list of strings for album titles/artists, for example, instead of just a list of Album objects.
* (We didn't do `save()` for that last title, so the last album title udpate didn't actually get saved in the database.)
* (I accidentally created a duplicate object. I did `Album.objects.all().delete()` to delete all records (and hence remote duplicates) and then `Album.objects.all()` again to check that it actually cleared everything.)

## actually do the filtering

* `Album.objects.filter(id=5)` to filter by finding result(s) with id=5 (there should only be one or none)
* `Album.objects.filter(id=6)`
* `Album.objects.filter(artist__startswith='the ')` using double underscore to get entries with artists starting with 'the '

# admin interface
* `python manage.py createsuperuser` to create admin
* set username, email, password
* http://127.0.0.1:8000/admin/
* log in
* Go to app1/admin.py to set up admin access to be able to see and edit databases.
  * Register Album in admin site.
* http://127.0.0.1:8000/admin/ (refresh)
  * You should see App1.
  * You can click on Albums to see the records.
  * You can click on a record to edit its contents.

# create another view
* (Note: view = function that takes a request and returns html)
* (Note: each view is linked to a URL pattern.)
* (Note: each URL is linked to an HTML response/page.)
* Edit app1/urls.py (to find pattern matches for requests) and app1/views.py (to define actions for requests).

# connect request/response to database
* Make app1/views.py import Album from .models
* In app1/views.py, you can type `all_albums = Album.objects.all()`, just like in the shell!
* http://127.0.0.1:8000/app1/ to see all albums
  * (Try going to details pages too.)
* (Note: we want to be able to separate the html from the python code for "separation of concerns".)

# create template
* (Note: Use templates to separate front-end HTMl/CSS files etc. from back-end Python files.)
* Create template HTML file app1/templates/app1/index.html:
  * Navigate to website (sub)folder (the one with manage.py in it).
  * `mkdir app1/templates/`
  * `mkdir app1/templates/app1`
  * `touch app1/templates/app1/index.html`
  * Create template code (see index.html), using html but also a for loop in "kinda python" code inside that html file.
* Open and write in app1/templates/app1/index.html
* Have app1/views.py make use of that template:
  * `from django.template import loader` to be able to load separate template files.
    * (Note: don't need this in later shortcut tutorial.)
  * Get database data, get template, get data to put into template, return filled template as HTML response.
* http://127.0.0.1:8000/app1/ to see it in action.

# shortcut for load-render template
* `from django.shortcuts import render` in app1/views.py so you can use render()
* http://127.0.0.1:8000/app1/

# activate 404 HTTP error page + message
* Create and make template HTML file app1/templates/app1/detail.html
* app1/views.py `from django.http import Http404` and edit `detail()`.
* Go to http://127.0.0.1:8000/app1/ and try clicking on albums to see details.
* Try going to 127.0.0.1:8000/app1/54 (or an id that doesn't exist).

# add entries to database
* (We're going to add a song to an album.)
* Add to app1/models.py class Song the function `__str__()`.
  * (Note: don't have to migrate / synch database because not adding attributes / columns.)
* Add to app1/admin.py import Song model and register Song model in admin site.
* http://127.0.0.1:8000/admin/ and check Songs

and then create song, set attributes, and save it:

```
python manage.py shell
from app1.models import Album, Song
album1 = Album.objects.get(id=5)
album1.artist # should return 'the new boston'
song = Song() # requires album, file_type, song_title
song.album = album1
song.file_type = 'mp3'
song.song_title = 'some title'
song.save()
```

* http://127.0.0.1:8000/admin/app1/song/ should show that song in there.

## oooor do that in one step with the create function:

(continuing with the same shell)

```
album1.song_set.all() # to see it so far
album1.song_set.create(song_title='I love bacon', file_type='mp3') # album already specified
album1.song_set.create(song_title='ice cream', file_type='mp3') # album already specified
```

* http://127.0.0.1:8000/admin/app1/song/ should show those new songs in there.

```
song = album1.song_set.create(song_title='hamburger', file_type='mp3') # make use of returned reference to that song
song.album
song.song_title
album1.song_set.all() # to see all songs in album1
album1.song_set.count() # gets size of set
```

# design the details.html template
* Edit app1/templates/app1/detail.html
* Refer to app1/models.py for the classes and corresponding variables.
* http://127.0.0.1:8000/app1/5/ should now show the image and other info available.

# remove hardcoded URLs (i.e. completely dynamic URLs)
* (I.e. make URLs completely dynamic, in case website structure changes.)
* (Note: app1/urls.py is a centralized place to edit the URL structure of the website.)
  * (Note: The `='index'` in `url(r'...', views...., name='index'),` gives the URL pattern the name 'index', so other files can refer to it.)
* Edit app1/templates/app1/index.html
  * `href="{% url 'detail' album.id %}/"` means to use URL pattern named detail and give it parameter variable album.id
* http://127.0.0.1:8000/app1/ and try going to one of the albums.

# namespaces / pattern reuse
* (Example: so we can reuse 'detail' pattern in both music/detail and video/detail, but need to specify which one.)
* Add app namespace `app_name = 'app1'` to app1/urls.py
* Use that namespace in app1/templates/index.html:
  * `href="{% url 'detail' album.id %}"` becomes `href="{% url 'app1:detail' album.id %}"`.
  * I.e. `'detail'` becomes `'app1:detail'`. Means to look for app1 detail pattern instead of just a generic detail pattern.
* (Note to self: can now reuse patterns.)

# HTTP 404 shortcut
* Import get_object_or_404 in app1/views.py
* `album = get_object_or_404(Album, pk=album_id)` replaces a whole try/except statement in detail().

# create form (in the easiest way to understand anyways)
* Make app1/models.py Song class have another attribute: `is_favourite`
* Make change file: `python manage.py makemigrations app1`
* Apply change to database: `python manage.py migrate`
* Restart server: Ctrl+C and then `python manage.py runserver` (in that separate Terminal).
* Refresh a view like http://127.0.0.1:8000/app1/5/ to see no errors.

You might want to have a URL that doesn't link to a template, like a "logging out" page that runs and then automatically redirects to another page.
* App a favourite URLs pattern in app1/urls.py

Actually make the form:
* Create a `<form>` in app1/templates/app1/detail.html view
  * `action="..."` is the URL pattern to send data to: `action="{% url 'app1:favourite' album.id %}"`
  * `method="post"`
  * `csrf_token` is for security [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
  * Loop through form elements. `{{ forloop.counter }}` auto-increments.
  * `name="..."` enables reference in the code.
* (Note: detail.html's action will go to urls.py to find the URL pattern for app1:favourite)
* (Note: URL pattern for app1:favourite will go to views.py to find favourite())
* Add function favourite() in app1/views.py
* Refresh a view like http://127.0.0.1:8000/app1/5/.
* Try favouriting a couple songs.
* (Note to self: detail.html loop to generate form --> associate each song with song.id --> user selects song + hits favourite --> app1:favourite --> urls.py views.favourite --> views.py favourite())
* (Note to self: song.id --> selected_song.is_favourite --> selected_song.save() --> redirect back to same page as if didn't leave)
