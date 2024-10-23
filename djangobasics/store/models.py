import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Article(models.Model):
    article_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='store/files/product_images')
    pub_date = models.DateTimeField("date published", default=timezone.now())
    def __str__(self):
        return self.article_name
    def date_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class CartItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.quantity} x {self.article.article_name}'