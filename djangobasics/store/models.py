import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now())
    def __str__(self):
        return self.article_name
    def date_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)