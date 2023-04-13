from django.shortcuts import render
from .models import Contents
from django.core.paginator import Paginator

# トップページ表示クラス
def index(request):
    # 新着の投稿
    latest_brog_article = Contents.objects.order_by('created_at')[0]
    # 人気の記事
    popular_blog_article = Contents.get_popular_article(Contents)
    context = {'article':latest_brog_article, 'list':popular_blog_article}
    return render(request, 'PhoenixBlog/index.html', context)

# 一覧ページ表示クラス
def list(request):
    # 記事一覧
    article_list = Contents.objects.all()
    # ページネーション
    paginator = Paginator(article_list, 10)  # 1ページあたり10件表示する
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'PhoenixBlog/list.html', {'posts': posts})
