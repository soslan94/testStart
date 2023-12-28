from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.author')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    title = [UniqueValidator(queryset=Article.title)]

    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'created_at', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.owner')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'article']