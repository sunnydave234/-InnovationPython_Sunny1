from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import BlogForm



# Create your views here.
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticate:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}

    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    blogname = Blog.objects.all()
    return render(request, 'accounts/home.html', {'blogname': blogname})

@login_required(login_url='login')
def createBlog(request):

    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/forms.html', context)

@login_required(login_url='login')
def updateBlog(request, pk):

    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    context = {'form':form}

    if request.method == 'POST':

        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'accounts/forms.html', context)

@login_required(login_url='login')
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('home')
    context = {'item':blog}
    return render(request, 'accounts/delete.html', context)