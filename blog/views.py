# blog/views.py
import django.views.generic
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .models import Post


class LoginView(django.views.generic.View):
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


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
