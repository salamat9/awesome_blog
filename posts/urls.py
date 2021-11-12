from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/comment_edit/<int:comment_pk>/', views.comment_edit, name='comment_edit'),  # new
    path('<int:pk>/post_like/', views.like_list, name='like_list'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.post_list, name='post_list')
]
