# views.py
from django.shortcuts import render
from .models import Post
from django.views import generic 

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'  # Explicitly set context name


class PostDetail(generic.DetailView):  # Renamed from DetailView to PostDetail
    model = Post
    template_name = 'post_detail.html'
