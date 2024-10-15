from django.db import models

class Articles(models.Model):
    article_name = models.CharField(max_length=200)
