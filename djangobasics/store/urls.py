from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "store"
urlpatterns = [
    path("index", views.index, name="index"),
    path("articles/<int:article_id>/", views.detail, name="article_detail"),
    path("articles/create/", views.article_create, name="article_create"),
    path("accounts/login/", auth_views.LoginView.as_view, name="login")
]