from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdatetView,
    ArticleDetailView,
    ArticleDeletetView,
)

urlpatterns = [
    path('/edit/',
         ArticleUpdatetView.as_view(), name = 'article_edit'),
    path('<int:pk>/',
         ArticleDetailView.as_view(), name = 'article_detail'),
    path('/delete/',
         ArticleDeletetView.as_view(), name = 'article_delete'),
    path('', ArticleListView.as_view(), name = 'article_list'),
]