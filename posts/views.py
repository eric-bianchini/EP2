from django.http import HttpResponseRedirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from .temp_data import post_data
from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from django.utils import timezone


def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_data = Comment.objects.filter(post=post_id)
    context = {'post': post,  'comment_list':reversed(comment_data)}
    return render(request, 'posts/detail.html', context)


def list_posts(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'posts/index.html', context)


def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(text__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)


def create_post(request):
    if request.method == 'POST':
        post_title = request.POST['title']
        post_text = request.POST['text']
        author_id = request.POST['author']
        post_author = User.objects.get(id=author_id)
        post = Post(author = post_author, title=post_title, text=post_text,
                      date = datetime.now())
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/create.html', context)


def update_post(request, post_id):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=post_id)
            post.title = request.POST['title']
            post.date = datetime.now()
            post.text = request.POST['text']

            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))

    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post, date = datetime.now())
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)
