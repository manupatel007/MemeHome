from django.urls import path, include
from . import views


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("",views.home, name="home"),
    path("register/", views.sign_up, name="signup"),
    path("create/", views.create_task, name="createtask"),
    path("show/", views.view_task, name="viewtask")
]