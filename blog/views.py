from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'HKK',
        'title': 'Blog Post #1',
        'content': 'First Blog Post',
        'date_posted': 'March 3, 2020'
    },
    {
        'author': 'BK',
        'title': 'Blog Post #2',
        'content': 'Second Blog Post',
        'date_posted': 'March 3, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
