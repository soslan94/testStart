from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField(max_length=100000, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

