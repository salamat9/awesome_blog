from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list')
]
