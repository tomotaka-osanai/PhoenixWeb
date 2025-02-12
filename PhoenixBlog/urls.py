from django.urls import path
from .views import IndexView, ListView, DetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', ListView.as_view(), name='list'),
    path('<int:content_id>/', DetailView.as_view(), name='detail'),
]
