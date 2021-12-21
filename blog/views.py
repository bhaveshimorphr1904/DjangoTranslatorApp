from django.shortcuts import render
from .models import Post
from django.views import generic

from blog import models

# Create your views here.


class BlogView(generic.DetailView):  # TemplateView when we work with data or model
    model = Post  # mode need only when we need data from DB
    template_name = 'blog.html'


class AboutView(generic.TemplateView):  # TemplateView when we work without data or model
    template_name = 'about.html'


class HomeList(generic.ListView):  # ListView when we work with data and list of model
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'
