from django.shortcuts import render
from .models import Post

posts=[
    {
        'author' : 'Mark Twain',
        'title' : '1st Post',
        'content' : 'First Post',
        'date_posted' : 'August 7th, 1989'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post 2',
        'content' : 'Second Post',
        'date_posted' : 'August 7th, 1999'
    }

]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About' } )
