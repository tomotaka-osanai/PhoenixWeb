from django.shortcuts import render
from .models import Article
from django.views.generic import ListView
from django.utils import timezone
from django.core.paginator import Paginator

# トップページ表示クラス
def index(request):
    latest_brog_article = Article.objects.order_by('created_at')[0]
    popular_blog_article = get_queryset()
    context = {'article':latest_brog_article, 'list':popular_blog_article}
    return render(request, 'PhoenixBlog/index.html', context)

# 一覧ページ表示クラス
def list(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 10)  # 1ページあたり10件表示する
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'PhoenixBlog/list.html', {'posts': posts})

# 人気の記事を10記事取得
def get_queryset():
    # 現在日時より過去の記事の中からランダムに10件を取得
    return Article.objects.filter(updated_at__lte=timezone.now()).order_by('?')[:10]
