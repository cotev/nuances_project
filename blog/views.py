from datetime import datetime


from django.shortcuts import render
from django.shortcuts import redirect


from blog.models import News
from blog.models import Story
from blog.models import StoryPage
from blog.models import Sketch
from blog.forms import ContactForm
from blog.forms import CommentForm
from blog.forms import SketchCommentForm
from blog.models import Comment
from blog.models import ItemCommonInfo


def view_home(request):
    list_news = News.objects.order_by('-date')

    return render(request, 'blog/home.html', {
        'list_news': list_news,
        })


def view_sketches(request):
    list_sketches = Sketch.objects.order_by('-date')

    return render(request, 'blog/sketches.html', {
        'list_sketches': list_sketches,
        })


def view_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        contact = form.save(commit=False)
        contact.date = datetime.today()
        contact.save()
        bool_sent = True

    return render(request, 'blog/contact.html', locals())


def view_stories(request):
   #list_stories = Story.objects.all() #I used to use this instruction but I have to order by the date from the most recent to the lattest.
    list_stories = Story.objects.order_by('-date')

    return render(request, 'blog/stories.html', {
        'list_stories': list_stories,
        })


def view_show_story(request, id_title):
    #This view find a story in the data base, using id_story and show the page show_story.html

    #ToDo : what happends when the title isn't right ? ==> make sure that can't happend.
    story = Story.objects.get(title=id_title)
    pages = story.storypage_set.all() #REMARQUE : they must not have capitals before the _set

    return render(request, 'blog/show_story.html', {
        'story': story,
        'pages': pages,
        })


#@ToDo : manage the else case when then form isn't valid.
def view_comment(request,id_title, id_comment_type):
    #We create a CommentForm or collect the data from the form through the POST method 
    form = CommentForm(request.POST or None)
    bool_sent = False #instruction needed for the block which manages the redirect, at the end of view_comment
    if id_comment_type == 'story':
        story = Story.objects.get(title=id_title)
        list_comments = story.comment_set.all()
        bool_story_comment = True
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.save()
            bool_sent = True
    elif id_comment_type == 'sketch':
#       sketch = Sketch.objects.get(title=id_title)
#       list_comments = sketch.comment_set.all()
        bool_sketch_comment = True
        if form.is_valid():
            comment = form.save(commit=False)
#           comment.sketch = sketch
            comment.save()
            bool_sent = True
    else:
        pass
        #What should I do ?
        #raise a 404 page error

    #this block is for going back to the story/sketch page when the comment has been sent
    #I should see if I keep it of not | 20170214
    if bool_sent:
        if id_comment_type == 'story':
            return redirect(view_show_story, id_title=id_title)
        if id_comment_type == 'sketch':
#           return redirect(view_sketches)
            return redirect(view_show_story, id_title=id_title)
    else:
        return render(request, 'blog/comment.html', locals())

#def view_sketch_comment(request, id_type):
def view_sketch_comment(request, id_type, id_title):
#def view_sketch_comment(request, id_title):
#def view_sketch_comment(request):
    form = SketchCommentForm(request.POST or None)
#   #Instruction needed for the block which manages
#   #the redirect, at the end of view_comment
    bool_sent = False

#   item = ItemCommonInfo.objects.get(title=id_title)
#   comments_list = item.sketchcomment_set.all()

#   We figure out what kind of item we comment
    if id_type == "Sketch":
         item = Sketch.objects.get(title=id_title)
         url_template = 'blog/sketch_comment.html'
         comments_list = ItemCommonInfo.objects.get(title=id_title).sketchcomment_set.all()


#   We figure out what kind of item we comment
#   if id_type == "Sketch":
#        item = Sketch.objects.get(title=id_title)
#        url_template = 'blog/sketch_comment.html'
#        comments_list = item.comments_list

#   item = item_instance.objects.get(title=id_title)
#   item = Sketch.objects.get(title=id_title)
#   item = Sketch.objects.get(title=id_title)

    if form.is_valid():
        comment = form.save(commit=False)
        #useless?
        comment.save()
        bool_sent = True

#   return render(request, 'blog/sketch_comment.html', locals())
    return render(request, url_template, locals())
