from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
