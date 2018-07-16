from django.db import models

class ItemCommonInfo(models.Model):
    title = models.CharField(max_length=100, default='Item')
    author = models.CharField(max_length=30, default='Cotev')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date")

    class Meta:
        abstract = True


class Item(ItemCommonInfo):
    def __def__(self):
        return self.author


class Comment(ItemCommonInfo):
    author = models.CharField(max_length=100, default='Anonymous')
    message = models.TextField(blank=False)
    item = models.ForeignKey('Item',null=True, on_delete=models.CASCADE,)

    def __def__(self):
        return self.author


class Sketch(Item):
    sketch_image = models.ImageField(upload_to="sketches/")

    def __str__(self):
        return self.title


class Story(Item):
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


class News(ItemCommonInfo):
    message = models.TextField(blank=False)

    def __str__(self):
        return self.title
