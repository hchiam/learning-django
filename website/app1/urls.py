from django.conf.urls import url
from . import views # imports views.py from within same folder

urlpatterns = [
    # matches to default view, so goes to /music/:
    url(r'^$', views.index, name='index'),
    # r'^$' is default page with no request made for app1, and calls views.py function index()
    # using name='index' for cool stuff in a later tutorial vid
    
    # /music/712/ for example album id=712:
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # (?P<album_id>[0-9]+) will pass in the number as a parameter variable album_id to the response function
    # calls views.detail() and gives it these parameters: request, album_id
]
