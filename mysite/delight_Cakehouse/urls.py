from django.urls import path
from . import views
#from allauth.account.views import LoginView


urlpatterns = [
    path("", views.home, name="home"),
    path("cake/", views.Cakes, name="Cakes_Center"),
    path("cookie/", views.Cookie, name="Cookie_Base"),
]
