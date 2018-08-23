from django.conf.urls import url
from django.contrib.sitemaps.views import sitemaps

from blog import views

urlpatterns = [
    url(r'^home/?$', views.view_home, name ='home'),
    url(r'^stories/?$', views.view_stories, name='stories'),
    url(r'^animations/?$', views.view_animations, name='animations'),
    url(r'^story/(?P<id_title>[\w\s]*)/?$', views.view_show_story, name='show_story'),
    url(r'^sketches/?$', views.view_sketches, name='sketches'),
    url(r'^contact/?$', views.view_contact, name='contact' ),
    url(r'^comment/(?P<id_title>[\w\s]+)/?$', views.view_comment, name='comment'),
]

#I added this for sitemaps framework
#but maybe it is in the nuances_project's urls.py
path('sitemap.xml', sitemap, {'sitemaps':sitemaps},
    name='django.contrib.sitemaps.views.sitemap')
