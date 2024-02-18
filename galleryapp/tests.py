from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reservation, Notification, GraphicsCategory
from .views import set_reservation, get_notifications

class ReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser567', password='12345')
        self.category = GraphicsCategory.objects.create(category='Test Category')
        self.reservation = Reservation.objects.create(user=self.user, category=self.category, description='Test Reservation', is_canceled=False)

    def test_set_reservation(self):
        reservations = set_reservation(self.user, is_canceled=False)
        self.assertEqual(reservations.count(), 1)

    def test_get_notifications(self):
        message = 'Test notification'
        notification = get_notifications(self.user, message)
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(notification.notification, message)

    # Dodaj więcej testów w razie potrzeby

class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_existing(self):
        response = self.client.post(reverse('login_existing'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # Sprawdza przekierowanie po zalogowaniu

    # Dodaj więcej testów widoków w razie potrzeby

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = GraphicsCategory.objects.create(category='Test Category')

    def test_reservation_creation(self):
        reservation = Reservation.objects.create(user=self.user, category=self.category, description='Test Reservation', is_canceled=False)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(reservation.user, self.user)

    # Dodaj więcej testów dla modeli w razie potrzeby

# Dodaj więcej testów w razie potrzeby
