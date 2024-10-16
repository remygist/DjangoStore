from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_protect

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

@csrf_protect
def article_create(request):
    if request.method == "POST":
        article_name = request.POST.get("article_name")

        if article_name:
            new_article = Article(article_name=article_name)
            new_article.save()
            return redirect("store:index")
        else:
            return HttpResponse("Article name cannot be empty", status=400)
    return render(request, "store/create.html")
