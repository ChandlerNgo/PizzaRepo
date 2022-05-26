from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login, name="login"),
    path("menu", views.menu, name="menu"),
    path("order", views.order, name="order"),
    path("rewards", views.rewards, name="rewards"),
]