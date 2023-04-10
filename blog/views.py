# blog/views.py
from django.views.generic import ListView, DetailView # нове

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # нове
    model = Post
    template_name = 'post_detail.html'
