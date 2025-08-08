"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include 
from .views import (home, about,pw_protected_view,user_only_view,staff_only_view)
from auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('about/', about, name='about'),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
    path('protected/user-only/', user_only_view),
    path('protected/staff-only/', staff_only_view),
    path('protected/', pw_protected_view, name='pw_protected_view'),
    path('admin/', admin.site.urls),
]
