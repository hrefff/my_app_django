from django.urls import path
from .views import index, all_articles, detail_article, AddArticleView

urlpatterns = [
    path('', index, name='home'),
    path('articles/', all_articles, name='all_articles'),
    path('articles/<int:id>/', detail_article, name='detail_article'),
    # path('articles/add', add_article, name='add_article'),
    path('articles/add', AddArticleView.as_view(), name='add_article'),
    # path('articles/', ArticleListView.as_view(), name='articles'),
    # path('articles/add', AddArticleView.as_view(), name='add_article'),
]