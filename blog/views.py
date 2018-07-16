from datetime import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from blog.models import News
from blog.models import Story
from blog.models import StoryPage
from blog.models import Sketch
from blog.models import Comment
from blog.models import Item

from blog.forms import CommentForm


def view_home(request):
    list_news = News.objects.order_by('-date')

    return render(request, 'blog/home.html', {
        'list_news': list_news,
        })


def view_sketches(request):
    sketches_list = Sketch.objects.order_by('-date')

    return render(request, 'blog/sketches.html', {
        'items_list': sketches_list,
        })


def view_animations(request):
    return render(request, 'blog/animations.html', locals())


def view_contact(request):
    return render(request, 'blog/contact.html', locals())


def view_stories(request):
    stories_list = Story.objects.order_by('-date')

    return render(request, 'blog/stories.html', {
        'items_list': stories_list,
        })


def view_show_story(request, id_title):
    story = Story.objects.get(title=id_title)
    pages = story.storypage_set.all()

    return render(request, 'blog/show_story.html', {
        'story': story,
        'pages': pages,
        })


def view_comment(request, id_title):
    form = CommentForm(request.POST or None)
    bool_sent = False
    item = Item.objects.get(title=id_title)
    comments_list = item.comment_set.all()

    if form.is_valid():
        comment = form.save(commit=False)
        comment.item = item
        comment.save()
        bool_sent = True

    return render(request, 'blog/comment.html', locals())
