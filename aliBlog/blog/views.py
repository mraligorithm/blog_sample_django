from django.shortcuts import render
from blog.models import Post, Comment
from blog.models import PostForm, CommentForm
from django.views.generic import (TemplateView,ListView,DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import login_required
from django.contrib.auth.decorators import LoginReqiredMixin


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView():
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginReqiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginReqiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post