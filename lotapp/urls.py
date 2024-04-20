from django.urls import path
from lotapp import views

urlpatterns = [
    path("", views.home, name="home"),
]