from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.category_detail, name='category_detail')
]