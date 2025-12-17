from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # [cite: 194]

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published' # [cite: 196-198]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # [cite: 201]
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # Менеджер для пошуку тільки опублікованих статей [cite: 328-330]
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='PB')

    objects = models.Manager() # Стандартний менеджер
    published = PublishedManager() # Наш спеціальний менеджер [cite: 334]

    class Meta:
        ordering = ['-publish'] # Сортування: нові зверху [cite: 208]
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title