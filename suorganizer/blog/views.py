from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  YearArchiveView, MonthArchiveView, ArchiveIndexView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .utils import PostGetMixin
from .forms import PostForm
from core.utils import UpdateView


class PostList(ArchiveIndexView):
    model = Post
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    paginate_by = 5
    template_name = 'blog/post_list.html'


class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostDetail(PostGetMixin, DetailView):
    allow_future = True
    queryset = (Post.objects
                .select_related('author__profile')
                .prefetch_related('tags')
                .prefetch_related('startups'))


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PostGetMixin, UpdateView):
    model = Post
    form_class = PostForm


class PostDelete(LoginRequiredMixin, PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')