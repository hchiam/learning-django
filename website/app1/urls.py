from django.conf.urls import url
from . import views # imports views.py from within same folder

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # r'^$' is default page with no request made for app1, and calls views.py function index()
]
