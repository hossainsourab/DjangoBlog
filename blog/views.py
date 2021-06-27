from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
# from django.views.generic.edit import CreateView


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Home'
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_dtl_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Detail Views'
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    success_url = '/success/'
    template_name = 'blog/post_creat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Post'
        return context


class PostSuccessMessageView(TemplateView):
    template_name = 'blog/success_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Success'
        return context
