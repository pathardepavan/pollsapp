from django.conf.urls import url
from django.contrib import admin
from .views import welcome,detail,vote
urlpatterns = [
    url(r'^$', welcome),
    url(r'^(?P<questionid>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<questionid>[0-9]+)/vote/$', vote, name='vote'),

]