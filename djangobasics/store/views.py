from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by("-pub_date")
    context = {
        "latest_articles_list": latest_articles_list,
    }
    return render(request, "store/index.html", context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "store/detail.html", {"article": article})

def article_create(request):
    return HttpResponse("This is the create article page!.")
