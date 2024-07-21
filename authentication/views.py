from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        password1 = form.data.get('password1')
        password2 = form.data.get('password2')
        if password1 != password2:
            messages.error(request,f"Passowrds do not match.")
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {user_name} , please log in now.")
            return redirect('login')
        

    context = {
        'form': form,
    }
    return render(request, 'authentication/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'{username} does not exist.')
    return render(request, 'authentication/login.html')
