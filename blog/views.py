from django.shortcuts import render
from .models import Post
from .forms import PostForm, ContactForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView


# from django.views.generic.edit import CreateView


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-created_at']
    paginate_by = 4

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


class PostDashboardView(ListView):
    model = Post
    context_object_name = 'total_post'
    ordering = ['-created_at']
    paginate_by = 3
    template_name = 'blog/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Dashboard'
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/success/'
    template_name = 'blog/update_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context


class Contact(CreateView):
    form_class = ContactForm
    success_url = '/success/'
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Contact'
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/dashboard/'
    template_name = 'blog/post_delete.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Blog | Contact'
    #     return context
