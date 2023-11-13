from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import post_data
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.contrib.auth.models import User

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
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
        return render(request, 'posts/create.html', {})


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.date = datetime.now()
        post.text = request.POST['text']

        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)