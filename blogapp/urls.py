from django.urls import path, include

from .views import ArticleListView, ArticleList, ArticleDetail, CommentList, CommentDetail


app_name = 'blogapp'


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article'),
    path('article_create', ArticleList.as_view(), name='article_create'),
    path('comments/', CommentList.as_view(), name = 'comment'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
]