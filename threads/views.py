from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Thread
from .forms import ThreadForm


@login_required(login_url="login")
def threads(request):
    threads = Thread.objects.all().order_by('-thread_date')
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        thread = form.save(commit=False)
        thread.thread_author = request.user
        thread.save()

    context = {
        'threads': threads,
        'form': form,
    }
    return render(request, 'threads/threads.html', context)


@login_required
def delete_thread(request, pk):
    thread = Thread.objects.get(id=pk)
    if request.user == thread.thread_author:
        thread.delete()
        return redirect('threads')
    else:
        return redirect('threads')


