from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm, NewsLinkForm
from .utils import PageLinksMixin, NewsLinkGetObjectMixin, StartupContextMixin
from core.utils import UpdateView


class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


class TagDetail(DetailView):
    queryset = (Tag.objects.prefetch_related('startup_set'))


class TagCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = TagForm
    model = Tag
    permission_required = 'organizer.add_tag'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, UpdateView):
    form_class = TagForm
    model = Tag


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5


class StartupDetail(DetailView):
    queryset = (Startup.objects
                .prefetch_related('tags')
                .prefetch_related('blog_posts')
                .prefetch_related('newslink_set'))


class StartupCreate(LoginRequiredMixin, CreateView):
    form_class = StartupForm
    model = Startup


class StartupUpdate(LoginRequiredMixin, UpdateView):
    form_class = StartupForm
    model = Startup


class StartupDelete(LoginRequiredMixin, DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')


class NewsLinkCreate(LoginRequiredMixin, NewsLinkGetObjectMixin, StartupContextMixin, CreateView):
    form_class = NewsLinkForm
    model = NewsLink

    def get_initial(self):
        startup_slug = self.kwargs.get(self.startup_slug_url_kwarg)
        self.startup = get_object_or_404(Startup, slug__iexact=startup_slug)
        initial = {self.startup_context_object_name: self.startup}
        initial.update(self.initial)
        return initial


class NewsLinkUpdate(LoginRequiredMixin, NewsLinkGetObjectMixin, StartupContextMixin, UpdateView):
    model = NewsLink
    form_class = NewsLinkForm
    slug_url_kwarg = 'newslink_slug'


class NewsLinkDelete(LoginRequiredMixin, NewsLinkGetObjectMixin, StartupContextMixin, DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return self.object.startup.get_absolute_url()
