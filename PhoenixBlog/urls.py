from django.urls import path
from .views import index, list, detail

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('<int:content_id>/', detail, name='detail'),
]
