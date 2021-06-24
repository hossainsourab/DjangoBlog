from django.shortcuts import render


# Create your views here.
def home(request):
    dicts = {'title': 'Blog | Home'}
    return render(request, 'blog/home.html', context=dicts)
