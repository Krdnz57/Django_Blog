from django.shortcuts import render
from .models import Post
import datetime

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def time(request):
    myDate = datetime.datetime.now()
    return render(request, 'blog/base.html', {'myDate': myDate})
