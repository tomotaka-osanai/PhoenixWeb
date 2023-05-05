from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    parent_category = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Contents(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_popular_article(self):
        # 現在日時より過去の記事の中からランダムに10件を取得
        return self.objects.filter(updated_at__lte=timezone.now()).order_by('?')[:10]

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.IntegerField(null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class ContentArticle(models.Model):
    content = models.IntegerField()
    article = models.IntegerField()
    class Meta:
        unique_together = ('content', 'article')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image_url = models.CharField(max_length=255)
    stock = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
