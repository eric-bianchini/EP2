from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.search_posts, name='search'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.PostDeleteView.as_view(), name='delete'),
]
