"""sports_event_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/cars/', include('cars.urls')),
    path('api/sports/', include('sports.urls')),
    path('api/locations/', include('locations.urls')),
    path('api/competitiveness_levels/', include('competitiveness_levels.urls')),
    path('api/skill_levels/', include('skill_levels.urls')),
    path('api/favorite_sports/', include('favorite_sports.urls')),
    path('api/sports_events/', include('sports_events.urls')),
    path('api/attending_athletes/', include('attending_athletes.urls')),
    path('api/event_message_boards/', include('event_message_boards.urls')),

]
