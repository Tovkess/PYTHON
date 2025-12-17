from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Список постів (використовуємо клас, як у завданні)
    path('', views.PostListView.as_view(), name='post_list'),

    # [cite_start]SEO-friendly посилання на пост [cite: 73-75]
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

    # Посилання для шерингу та коментарів
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]