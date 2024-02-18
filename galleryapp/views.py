from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import PhotoForm
from .models import Notification, Reservation

def set_reservation(user, is_canceled):
    reservations = Reservation.objects.filter(user=user, is_canceled=is_canceled)
    return reservations

def get_notifications(user, message):
    created_notification = Notification.objects.create(user=user, notification=message)
    return created_notification

def login_existing(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notifications')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            note = "Zostales zarejestrowany"
            get_notifications(note)
            login(request, user)
            return redirect('notifications')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_existing')

def reservations(request):
    if request.user.is_authenticated:
        is_canceled = False
        user = request.user
        reservations = set_reservation(user, is_canceled)
        return render(request, 'gallery.html', {'photos': reservations})
    return render(request, 'gallery.html', {'photos': []})

def cancelled_reservations(request):
    if request.user.is_authenticated:
        is_canceled = True
        user = request.user
        reservations = set_reservation(user, is_canceled)
        return render(request, 'gallery.html', {'photos': reservations})
    return render(request, 'gallery.html', {'photos': []})

def notifications(request):
    if request.user.is_authenticated:
        photos = Notification.objects.filter(user=request.user).order_by('upload_date')
        return render(request, 'gallery.html', {'photos': photos})
    return render(request, 'gallery.html', {'photos': []})

def add_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                photo.user = request.user
                note = "Zamowienie zostalo dokonane"
                get_notifications(note)
                photo.save()
                return redirect('reservations')
        else:
            form = PhotoForm()
        return render(request, 'add_photo.html', {'form': form})
    return redirect('login_existing')

def delete_photo(request, reservation_id):
    if request.user.is_authenticated:
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
            if reservation.user == request.user:
                reservation.delete()
                note = "Zamówienie zostało anulowane"
                get_notifications(note)
                return redirect('reservations')
            else:
                return redirect('reservations')
        except Reservation.DoesNotExist:
            return redirect('reservations')
    return redirect('login_existing')