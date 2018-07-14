from django.contrib import admin
from blog.models import Story
from blog.models import StoryPage
from blog.models import Contact
from blog.models import Sketch
from blog.models import Comment
from blog.models import News


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    list_filter = ('title','date',)


class StoryPageAdmin(admin.ModelAdmin):
    list_display = ('story', 'page_title', 'page_number',)
    list_filter = ('story',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'date', 'message',)
    list_filter = ('date',)


class SketchAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'sketch', 'comments_list',)
    list_filter = ('date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'message','date', 'story', 'sketch',)
    list_filter = ('date',)


admin.site.register(Story, StoryAdmin)
admin.site.register(StoryPage, StoryPageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News)
