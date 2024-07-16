from django.shortcuts import render
from .models import Posts
# Create your views here.


def index(request):
    posts = Posts.objects.all()
    return render(request, 'myapp/index.html', {'posts':posts})