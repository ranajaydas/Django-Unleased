from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

from .models import Startup


class BaseStartupFeedMixin:

    def description(self, startup):
        return "News related to {}".format(startup.name)

    def get_object(self, request, startup_slug):
        return get_object_or_404(Startup, slug__iexact=startup_slug)

    def items(self, startup):
        return startup.newslink_set.all()[:10]

    def item_description(self, newslink):
        return newslink.description()

    def item_link(self, newslink):
        return newslink.link

    def item_title(self, newslink):
        return newslink.title

    def link(self, startup):
        return startup.get_absolute_url()

    def subtitle(self, startup):
        return self.description(startup)

    def title(self, startup):
        return startup.name


class AtomPostFeed(BaseStartupFeedMixin, Feed):
    feed_type = Atom1Feed


class Rss2PostFeed(BaseStartupFeedMixin, Feed):
    feed_type = Rss201rev2Feed
