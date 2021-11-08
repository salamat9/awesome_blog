from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'list.html', {'posts': posts,
                                         'categories': categories})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})


def post_create(request):
    form = PostForm()
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('form')
            print(form)
            cd = form.cleaned_data
            print('cd')
            print(cd)
            Post.objects.create(title=cd['title'],
                                image=request.FILES['image'],
                                description=cd['description'],
                                body=cd['body'],
                                category=cd['category'],
                                author=request.user
                                )
            return redirect('post_list')
    return render(request, 'create.html', {'form': form})

