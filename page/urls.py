from django.urls import path
from .views import NewsFormView, NewsEditFormView, NewsDetailView, NewsListView

urlpatterns = [
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsFormView.as_view(), name='create_page'),
    path('<int:news_id>/edit/', NewsEditFormView.as_view(), name='edit_page'),
]
