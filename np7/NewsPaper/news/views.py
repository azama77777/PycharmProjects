from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'



