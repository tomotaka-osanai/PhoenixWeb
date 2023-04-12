from django.shortcuts import render
from .models import Article

def index(request):
    latest_brog_article = Article.objects.order_by('created_at')[0]
    context = {'article':latest_brog_article}
    return render(request, 'PhoenixBrog/index.html', context)
