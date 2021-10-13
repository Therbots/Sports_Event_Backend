from django.urls import path
from attending_athletes import views

urlpatterns = [
    path('', views.user_attending_athlete)
]