from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # Беремо тільки опубліковані пости
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    # Шукаємо пост за ID. Якщо немає - видасть помилку 404
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})