from django.db import models

class ItemCommonInfo(models.Model):
    title = models.CharField(max_length=100, default='Item')
    author = models.CharField(max_length=30, default='Cotev')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date")

    class Meta:
        abstract = True

#Should be named Item and subclassed
#ItemCommonInfo
class Item(ItemCommonInfo):
    def __def__(self):
        return self.author


#Should subclassed ItemCommonInfo
#class SketchComment(models.Model):
class Comment(ItemCommonInfo):
    author = models.CharField(max_length=100, default='Anonymous')
    message = models.TextField(blank=False)
    item = models.ForeignKey('Item',null=True, on_delete=models.CASCADE,)

    def __def__(self):
        return self.author


#class Sketch(ItemCommonInfo):
class Sketch(Item):
    sketch_image = models.ImageField(upload_to="sketches/")
    #useless?
    item_type = "Sketch"

    def __str__(self):
        return self.title


#class Story(models.Model):
#class Story(ItemCommonInfo):
class Story(Item):
#    title = models.CharField(max_length=100)
#    author = models.CharField(max_length=30)
#    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of publication")
    cover_page = models.ImageField(upload_to="covers/")
    #useless ?
#   item_type = "Story"

    def __str__(self):
        return self.title


class StoryPage(models.Model):
    page_number = models.IntegerField(default=0)
    page_title = models.CharField(max_length=100)
    page = models.ImageField(upload_to="pages/")
    story = models.ForeignKey('Story',null=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.page_title


#Should subclassed ItemCommonInfo
#class Contact(models.Model):
class Contact(ItemCommonInfo):
#   author = models.CharField(max_length=100)
    message = models.TextField(blank=False)
    email = models.EmailField()
#   date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of contact")

    def __str__(self):
        return self.author


#class Comment(models.Model):
#    author = models.CharField(max_length=100, default='Anonymous')
#    message = models.TextField(blank=False)
#    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of comment")
#    story = models.ForeignKey('Story', null=True, on_delete=models.CASCADE,)
##   sketch = models.ForeignKey('Sketch', null=True, on_delete=models.CASCADE,)
#
#    def __def__(self):
#        return self.author


#Should subclassed ItemCommonInfo
#class News(models.Model):
class News(ItemCommonInfo):
#    title = models.TextField(blank=True)
#    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of news")
    message = models.TextField(blank=False)

    def __str__(self):
        return self.title
