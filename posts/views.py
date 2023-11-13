from django.http import HttpResponseRedirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from .temp_data import post_data
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .forms import PostForm
from django.utils import timezone

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'


def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(text__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = '/posts'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'text' ]
    success_url = '/posts'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/posts'