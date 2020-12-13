from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleSearchListView,
    CommentCreateView,
    ArticleManageListView,
    ArticleManageSearchListView,
)

urlpatterns = [
    path('<uuid:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<uuid:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<uuid:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('search/', ArticleSearchListView.as_view(), name='search_results'),
    path('<uuid:pk>/comment/', CommentCreateView.as_view(), name='article_comment_add'),
    path('manage/', ArticleManageListView.as_view(), name='article_manage'),
    path('manage/search/', ArticleManageSearchListView.as_view(), name='article_manage_search'),
    path('', ArticleListView.as_view(), name='article_list')
]