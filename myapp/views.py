from django.shortcuts import render,redirect, get_object_or_404
from .models import Posts
# Create your views here.


def index(request):
    posts = Posts.objects.all()
    latest_posts = Posts.objects.all().order_by('-created_at')[:3]
    return render(request, 'myapp/index.html', {'posts':posts,'latest':latest_posts})


def post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'myapp/post.html', {'post':post})



def contact(request):
    return render(request, 'myapp/contact/contact.html')
