from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name='signup'),
    path("handle_login", views.handle_login, name='handle_login'),
    path("handle_logout", views.handle_logout, name='handle_logout'),
    path("all_passwords", views.all_passwords, name='all_passwords'),
    path("add_password", views.add_password, name='add_password'),
    path("update/<int:id>", views.update, name='update'),
    path("delete/<int:id>", views.delete, name='delete'),


]
