# blog/views.py
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Post, Bookmark


class LoginView(View):
    model = get_user_model()
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        logout(request)
        return redirect('home')


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # If user is logged in, provide context for bookmarks
            post = self.get_object()
            is_bookmarked = Bookmark.objects.filter(user=self.request.user, post=post).exists()
            context['is_bookmarked'] = is_bookmarked
        return context


@method_decorator(login_required, name='dispatch')
class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmarks.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class BookmarkAddView(View):
    @staticmethod
    def get(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        Bookmark.objects.get_or_create(user=request.user, post=post)

        return redirect('post_detail', pk=post.pk)


@method_decorator(login_required, name='dispatch')
class BookmarkRemoveView(View):
    @staticmethod
    def get(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        bookmark = Bookmark.objects.filter(user=request.user, post=post).first()
        if bookmark:
            bookmark.delete()

        return redirect('post_detail', pk=post.id)

