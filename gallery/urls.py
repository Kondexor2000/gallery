"""
URL configuration for gallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from galleryapp import views
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('login/', views.login_existing, name='login_existing'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)