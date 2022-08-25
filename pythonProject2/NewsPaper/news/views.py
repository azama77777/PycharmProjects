from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import *
from .filters import PostFilter
from datetime import datetime
from django.core.cache import cache


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'news/authors.html'
    paginate_by = 10


class PostList(ListView):
    model = Post
    ordering = 'title'
    context_object_name = 'posts'
    template_name = 'news/posts.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCreate(CreateView):
    form_class = PostForm
    model = Post


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
