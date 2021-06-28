"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', views.PostListView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('success/', views.PostSuccessMessageView.as_view(), name='success'),
    path('dashboard/', views.PostDashboardView.as_view(), name='dashboard'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),

    # Start Custom Authentication User


    # End Custom Authentication User

]
