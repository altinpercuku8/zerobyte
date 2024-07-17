from django.shortcuts import render
from .models import Posts
# Create your views here.


def index(request):
    posts = Posts.objects.all()
    latest_posts = Posts.objects.all().order_by('-created_at')[:3]
    return render(request, 'myapp/index.html', {'posts':posts,'latest':latest_posts})