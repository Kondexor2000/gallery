from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PhotoForm
from .models import Photo

def login_existing(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gallery')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('gallery')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('gallery')

def gallery(request):
    if request.user.is_authenticated:
        photos = Photo.objects.filter(user=request.user)
        return render(request, 'gallery.html', {'photos': photos})
    return render(request, 'gallery.html', {'photos': []})

def add_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                photo.user = request.user
                photo.save()
                return redirect('gallery')
        else:
            form = PhotoForm()
        return render(request, 'add_photo.html', {'form': form})
    return redirect('login_existing')

def delete_photo(request, photo_id):
    if request.user.is_authenticated:
        photo = Photo.objects.get(pk=photo_id)
        if photo.user == request.user:
            photo.delete()
        return redirect('gallery')
    return redirect('login_existing')