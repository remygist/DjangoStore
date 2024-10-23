from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

from .models import Article,CartItem


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "store/detail.html", {"article": article})

@csrf_protect
@login_required
def article_create(request):
    if request.method == "POST":
        article_name = request.POST.get("article_name")
        if Article.objects.filter(article_name=article_name).exists():
            return render(request, "store/create.html", {"error":"This article already exists."})
        elif article_name:
            new_article = Article(article_name=article_name)
            new_article.save()
            return redirect("store:index")
        else:
            return HttpResponse("Article name cannot be empty", status=400)
    return render(request, "store/create.html")

@login_required
def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        article.delete()
        return redirect("store:index")
    return render(request, 'store/article_confirm_delete.html', {'article': article})

def index(request):  
    latest_articles_list = Article.objects.order_by("-pub_date")

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.article.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    context = {
        "latest_articles_list": latest_articles_list,
        "cart_items": cart_items,
        "total_price": total_price
    }

    return render(request, "store/index.html", context)

def add_to_cart(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    cart_item, created = CartItem.objects.get_or_create(article=article, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('store:index')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('store:index')
