from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.sitemaps import PostSitemap
from organizer.sitemaps import TagSitemap, StartupSitemap


class RootSitemap(Sitemap):
    priority = 0.6

    def items(self):
        return [
            'about_site',
            'blog_post_list',
            'contact',
            'login',
            'organizer_startup_list',
            'organizer_tag_list',
        ]

    def location(self, url_name):
        return reverse(url_name)


sitemaps = {
    'posts': PostSitemap,
    'roots': RootSitemap,
    'tags': TagSitemap,
    'startups': StartupSitemap,
}
