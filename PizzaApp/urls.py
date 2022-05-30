from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login, name="login"),
    path("order", views.order, name="order"),
    path("rewards", views.rewards, name="rewards"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("termsandconditions", views.termsandconditions, name="termsandconditions"),
]