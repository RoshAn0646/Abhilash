# travel_experience/urls.py (main urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('experience/', include('ABHILASH.urls')),  # Add this line
]
