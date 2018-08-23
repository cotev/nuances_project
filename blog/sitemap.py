from django.contrib.sitemaps import Sitemap
from blog.models import item

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Item.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.date

