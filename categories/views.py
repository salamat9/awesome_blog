from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from posts.models import Post
from .forms import CategoryForm


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_detail.html', {'posts': posts,
                                                    'category': category})


def category_create(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Category.objects.create(name=cd['name'])
            return redirect('post_list')
    return render(request, 'category_create.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.POST:
        category.delete()
        return redirect('post_list')
    return render(request, 'category_delete.html', {'category': category})
