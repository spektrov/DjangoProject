# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView # нові зміни

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # нові зміни
    path('', BlogListView.as_view(), name='home'),
]
