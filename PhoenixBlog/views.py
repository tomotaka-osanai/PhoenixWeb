from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import PhoenixBlog, Contents, Article, ContentArticle, Category

from rest_framework import viewsets
from .serializers import PhoenixBlogSerializer

# 共通クラス


class PhoenixBlogView(viewsets.ModelViewSet):
    serializer_class = PhoenixBlogSerializer
    queryset = PhoenixBlog.objects.all()


class BaseView(TemplateView):
    # 共通処理を実装する場合はここに記述
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 共通の処理を実装する
        context['categories'] = Category.objects.all()
        return context

# トップページ表示クラス


class IndexView(BaseView):
    template_name = 'PhoenixBlog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 新着の投稿
        context['article'] = Contents.objects.order_by('created_at').first()
        # 人気の記事
        context['list'] = Contents.get_popular_article()
        return context

# 一覧ページ表示クラス


class ListView(BaseView):
    template_name = 'PhoenixBlog/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 記事一覧
        article_list = Contents.objects.all()
        # ページネーション
        paginator = Paginator(article_list, 10)  # 1ページあたり10件表示する
        page = self.request.GET.get('page')
        posts = paginator.get_page(page)
        context['posts'] = posts
        return context

# 詳細ページ表示クラス


class DetailView(BaseView):
    template_name = 'PhoenixBlog/detail.html'
    model = Contents
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # コンテンツ
        content = self.get_object()
        context['content'] = content
        # 記事
        # コンテンツに紐づく記事を取得
        content_article_ids = ContentArticle.objects.filter(
            content=content.id).values_list('article', flat=True)
        articles = Article.objects.filter(id__in=content_article_ids)
        context['articles'] = articles
        return context

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs.get('content_id'))
