# learning-django
Learning Django from [YouTube](https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)

# my older repo
https://github.com/hchiam/djangoApp

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

# create & activate models (how you want to store your data)
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

"""
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
"""
