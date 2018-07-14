from django.db import models


class ItemCommonInfo(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date")
    comments_list = []
#    def add_sketch_comment(author, message, date):
#        comment = SketchComment(author=author, message=message, date=date)
#        return comment

    class Meta:
        abstract = True


class SketchComment(models.Model):
    author = models.CharField(max_length=100, default='Anonymous')
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of comment")

    def __def__(self):
        return self.author


#Let's try first to change the comment structure for sketches
#just to see how it works.
class Sketch(ItemCommonInfo):
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of sketch")
    sketch = models.ImageField(upload_to="sketches/")
    #I just wonder if we can instance several SketchComment for 
    #one instance of Sketch.
#   comment() = SketchComment()

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of publication")
    cover_page = models.ImageField(upload_to="covers/")

    def __str__(self):
        return self.title


class StoryPage(models.Model):
    page_number = models.IntegerField(default=0)
    page_title = models.CharField(max_length=100)
    page = models.ImageField(upload_to="pages/")
    story = models.ForeignKey('Story',null=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.page_title



class Contact(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField(blank=False)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of contact")

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=100, default='Anonymous')
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of comment")
    story = models.ForeignKey('Story', null=True, on_delete=models.CASCADE,)
    sketch = models.ForeignKey('Sketch', null=True, on_delete=models.CASCADE,)

    def __def__(self):
        return self.author

class News(models.Model):
    title = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of news")
    message = models.TextField(blank=False)

    def __str__(self):
        return self.title
