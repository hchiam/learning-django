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
* Go to http://127.0.0.1:8000/ in your browser.
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
