from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^home/?$', views.view_home, name ='home'),
    url(r'^stories/?$', views.view_stories, name='stories'),
    url(r'^story/(?P<id_title>[\w\s]*)/?$', views.view_show_story, name='show_story'),
    url(r'^sketches/?$', views.view_sketches, name='sketches'),
    url(r'^contact/?$', views.view_contact, name='contact' ),
    url(r'^comment/(?P<id_title>[\w\s]+)/?$', views.view_comment, name='comment'),
]
