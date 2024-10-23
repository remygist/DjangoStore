from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="index"),
    path("articles/<int:article_id>/", views.detail, name="article_detail"),
    path("articles/create/", views.article_create, name="article_create"),
    path("articles/<int:article_id>/delete/", views.article_delete, name="article_delete"),
    path('add-to-cart/<int:article_id>/', views.add_to_cart, name='add_to_cart'),
    path("cart/remove/<int:item_id>", views.remove_from_cart, name="remove_from_cart"),
]