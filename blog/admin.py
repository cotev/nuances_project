from django.contrib import admin
from blog.models import Story
from blog.models import StoryPage
from blog.models import Sketch
from blog.models import Comment
from blog.models import News
from blog.models import Item
from blog.models import Animation


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    list_filter = ('title','date',)


class StoryPageAdmin(admin.ModelAdmin):
    list_display = ('story', 'page_title', 'page_number',)
    list_filter = ('story',)


class SketchAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'sketch_image', 'id')
    list_filter = ('date',)


class CommentAdmin(admin.ModelAdmin):
   list_display = ('author', 'message','date',)
   list_filter = ('date',)


class NewsAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'message','date',)
   list_filter = ('date',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    list_filter = ('date',)

class AnimationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'url',)
    list_filter = ('date',)


admin.site.register(Story, StoryAdmin)
admin.site.register(StoryPage, StoryPageAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Animation, AnimationAdmin)
