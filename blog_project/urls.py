# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include # нові зміни

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # нові зміни
]
