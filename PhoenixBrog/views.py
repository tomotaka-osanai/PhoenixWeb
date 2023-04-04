from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {'':''}
    return render(request, 'PhoenixBrog/index.html', context)
