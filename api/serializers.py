from django.db import transaction
from django.db.models import F
from rest_framework import serializers
from articlesapp.models import *


class ArticleSerializer(serializers.ModelSerializer):
    your_rating = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title', 'your_rating', 'rating_count', 'average_rating')

    def get_your_rating(self, obj):
        try:
            return ArticleRating.objects.get(article=obj, user=self.context["request"].user).rating
        except Exception as e:
            return "-"


class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = ('rating',)

    def create(self, validated_data):
        user = self.context['request'].user
        article_id = self.context['view'].kwargs["article_id"]
        print(user, article_id)

        with transaction.atomic():
            article_rating = ArticleRating.objects.create(article_id=article_id, user=user,
                                                          rating=validated_data["rating"])
            Article.objects.filter(id=article_id).update(rating_count=F("rating_count") + 1,
                                                         rating_sum=F("rating_sum") + validated_data["rating"])
            return article_rating

    def update(self, instance, validated_data):
        article_id = self.context['view'].kwargs["article_id"]

        with transaction.atomic():
            Article.objects.filter(id=article_id).update(
                rating_sum=F("rating_sum") - instance.rating + validated_data["rating"])

            return super().update(instance, validated_data)
