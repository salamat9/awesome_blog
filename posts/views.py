from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404, NoReverseMatch
from django.contrib.auth.decorators import login_required
from .forms import PostForm, PostEditForm, CommentForm
from .models import Post, Category, Comment


@login_required(login_url='login')
def like(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user not in post.likes.all():
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    return redirect(post.get_absolute_url())


@login_required(login_url='login')
def like_list(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user not in post.likes.all():
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    return redirect('post_list')


def is_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if request.user.id == post.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(post.get_absolute_url())
    return _wrapped_view


def is_comment_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        comment = Comment.objects.get(pk=kwargs['comment_pk'])
        print(kwargs)
        if request.user.id == comment.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(post.get_absolute_url())
    return _wrapped_view


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
                                           'comments': comments})  # new

@login_required(login_url='login')
def post_create(request):
    form = PostForm()
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Post.objects.create(title=cd['title'],
                                image=request.FILES['image'],
                                description=cd['description'],
                                body=cd['body'],
                                category=cd['category'],
                                author=request.user
                                )
            return redirect('post_list')
    return render(request, 'create.html', {'form': form})


@is_author
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


@is_author
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST:
        post.delete()
        return redirect('post_list')
    return render(request, 'delete.html', {'post': post})


@is_comment_author
def comment_edit(request, pk, comment_pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.POST:
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm(
            initial={
                'content': comment.content
            }
        )
    return render(request, 'comment_edit.html', locals())




