from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add-post', views.ArticleCreateView.as_view(), name='add-post'),
    path('add-category', views.CategoryCreateView.as_view(), name='add-category'),
    path('article/edit/<int:pk>/', views.ArticleUpdateView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', views.ArticleDeleteView.as_view(), name='delete-post'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('count/<int:pk>/', views.BlogPostDetail, name='count-like'),
    path('create/<int:pk>/comment', views.CommentCreateView.as_view(), name='create-comment'),
]