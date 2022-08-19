from django.urls import path
from .views import HomePageView, BlogListView, BlogDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]