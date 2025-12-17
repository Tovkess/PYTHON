from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag # Для тегів
from django.db.models import Count # Для підрахунку схожих

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    
    # Якщо передано тег - фільтруємо пости
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    return render(request, 'blog/post/list.html', {'posts': posts, 'tag': tag})

def post_detail(request, id): # Якщо у вас тут (year, month, day, post), залиште як було, але додайте код нижче
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
    # Логіка для схожих постів
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'blog/post/detail.html', 
                  {'post': post, 'similar_posts': similar_posts})