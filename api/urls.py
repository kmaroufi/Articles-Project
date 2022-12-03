from django.urls import path, include

from api.views import ArticleList, ArticleRatingCreateOrUpdate

app_name = "api"

urlpatterns = [
    path('articles', ArticleList.as_view(), name="articles"),
    path('articles/<int:article_id>/rate', ArticleRatingCreateOrUpdate.as_view(), name="article_rating"),
]