"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Users import views as User_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    #for first two is for login and logout views, redirect to template by passing it as argument for template_name function
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name = '/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/logout.html'), name='Log Out'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = '/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/login.html'), name='Log In'),
    path('accounts/profile/', User_views.profile, name='Profile'),
    path("admin/", admin.site.urls),
    path('register/', User_views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path("", include ("delight_Cakehouse.urls")),
    path("home/", include ("delight_Cakehouse.urls")),
    path("cake/", include ("delight_Cakehouse.urls")),
    path("cookie/", include ("delight_Cakehouse.urls")),
]
