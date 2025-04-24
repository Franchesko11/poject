from django.urls import path
from .views import (
    NewsListView, NewsSearchView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]