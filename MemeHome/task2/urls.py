from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.hierarchy_view, name="hierarchy")
]