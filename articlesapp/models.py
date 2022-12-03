from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating_count = models.PositiveIntegerField(default=0)
    rating_sum = models.PositiveIntegerField(default=0)

    def average_rating(self):
        return f"{(self.rating_sum / self.rating_count):.2f}" if self.rating_count > 0 else "-"


class ArticleRating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

