from django.shortcuts import render

from .models import Post, Category


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'list.html', {'posts': posts,
                                         'categories': categories})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})
