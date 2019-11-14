from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  YearArchiveView, MonthArchiveView, ArchiveIndexView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm
from .utils import PostGetMixin
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
    model = Post
    allow_future = True


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post


class PostUpdate(LoginRequiredMixin, PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post


class PostDelete(LoginRequiredMixin, PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')