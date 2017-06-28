from django.conf.urls import url
from . import views # imports views.py from within same folder

app_name = 'app1'

urlpatterns = [
    # matches to default view, so goes to /music/:
    url(r'^$', views.index, name='index'),
    # r'^$' is default page with no request made for app1, and calls views.py function index()
    # name='index' names this url pattern for referring to when removing hardcoded URLs (completely dynamic-ifying)
    
    # /app1/<album_id>/
    # /app1/712/ for example album id=712:
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # (?P<album_id>[0-9]+) will pass in the number as a parameter variable album_id to the response function
    # calls views.detail() and gives it these parameters: request, album_id
]
