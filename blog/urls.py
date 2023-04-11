# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView, LoginView, LogoutView,\
    BookmarkAddView, BookmarkListView, BookmarkRemoveView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('bookmarks/', BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmark/add/<int:post_id>/', BookmarkAddView.as_view(), name='bookmark_add'),
    path('bookmark/remove/<int:post_id>/', BookmarkRemoveView.as_view(), name='bookmark_remove'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', BlogListView.as_view(), name='home'),
]
