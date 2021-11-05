from django.shortcuts import render
from .models import Category
from posts.models import Post


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category,
                                                    'posts': posts})
