from django.urls import path
from . import views


urlpatterns = [
    path("", views.weather_view, name="home"),
    path("history", views.records, name="history"),
]
