from django.contrib import admin

from .models import Article, CartItem

admin.site.register(Article)
admin.site.register(CartItem)
