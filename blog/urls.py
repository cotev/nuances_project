from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^home/?$', views.view_home, name ='home'),
    url(r'^stories/?$', views.view_stories, name='stories'),
    url(r'^story/(?P<id_title>[\w\s]*)/?$', views.view_show_story, name='show_story'),
    url(r'^sketches/?$', views.view_sketches, name='sketches'),
    url(r'^contact/?$', views.view_contact, name='contact' ),
    url(r'^comment/story/(?P<id_title>[\w\s]+)/?$', views.view_comment, {'id_comment_type' : 'story'}, name='comment_story'),
#   url(r'^comment/sketch/(?P<id_title>[\w\s]+)/?$', views.view_comment, {'id_comment_type' : 'sketch'}, name='comment_sketch'),
#   url(r'^comment/sketch_bis/(?P<id_type>[\w\s]+)/(?P<id_title>[\w\s]+)/?$', views.view_sketch_comment, name='sketch_comment'),
#   url(r'^comment/sketch_bis/(?P<id_title>[\w\s]+)/?$', views.view_sketch_comment, name='sketch_comment'),
#   url(r'^comment/sketch_bis/?$', views.view_sketch_comment, name='sketch_comment'),
]
