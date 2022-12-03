from django.contrib import admin

# Register your models here.
from .models import Article, ArticleRating


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(ArticleRating)
class ArticleRatingAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'rating')