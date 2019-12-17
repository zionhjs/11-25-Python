from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('login_verify', views.login_verify),
    path('logout', views.logout),
    path('register', views.register),
    path('register_verify', views.register_verify),
    path('clockinout', views.clockinout),
]