from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('create/', views.category_create, name='category_create')
]