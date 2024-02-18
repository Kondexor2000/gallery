from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class GraphicsCategory(models.Model):
    category = models.CharField(max_length=100)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(GraphicsCategory, on_delete=models.CASCADE)
    description = models.TextField()
    is_canceled = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
class Notification(models.Model):
    notification = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)