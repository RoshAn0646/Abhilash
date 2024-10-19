# ABHILASH/urls.py
from django.urls import path
from .views import travel_experience_view

urlpatterns = [
    path('', travel_experience_view, name='travel_experience'),
]
