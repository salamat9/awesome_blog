from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, PostEditForm, CommentForm
from .models import Post, Category, Comment


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'list.html', {'posts': posts,
                                         'categories': categories})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                author=request.user,
                post=post,
                content=cd['content']
            )
            return redirect(post.get_absolute_url())
    return render(request, 'detail.html', {'post': post,
                                           'form': form,
                                           'comments': comments})


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


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST:
        form = PostEditForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostEditForm(
            initial={
                'title': post.title,
                'description': post.description,
                'body': post.body,
                'image': post.image,
                'category': post.category
            }
        )
    return render(request, 'edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST:
        post.delete()
        return redirect('post_list')
    return render(request, 'delete.html', {'post': post})




