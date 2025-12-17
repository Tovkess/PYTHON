from django.urls import path
from . import views
from .feeds import LatestPostsFeed # RSS

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'), # Пошук по тегу [cite: 84]
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'), # Стрічка новин [cite: 361]
]