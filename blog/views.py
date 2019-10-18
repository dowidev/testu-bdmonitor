from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Post, Update


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class UpdateListView(ListView):
    model = Update
    template_name = 'update.html'
    context_object_name = 'all_updates_list'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['requirement', 'user1', 'author', 'dir_ap', 'requirement_type', 'prioritas', 'target', 'budget']


class UpdateCreateView(CreateView):
    model = Update
    template_name = 'update_new.html'
    fields = ['posting', 'author', 'last_update', 'progress', 'status', 'status_akhir']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['requirement', 'user1', 'author', 'dir_ap', 'requirement_type', 'prioritas', 'target', 'budget']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

