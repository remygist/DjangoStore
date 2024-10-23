from django.contrib import admin

from .models import Article, CartItem

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(Article, ArticleAdmin)
admin.site.register(CartItem)
