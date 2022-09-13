from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ArticleList(ListView):
    model = Article
    ordering = 'title'
    context_object_name = 'articles'
    template_name = 'articles/posts.html'
    paginate_by = 4
