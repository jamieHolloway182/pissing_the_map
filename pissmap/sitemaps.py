from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PissmapSitemap(Sitemap):
    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)