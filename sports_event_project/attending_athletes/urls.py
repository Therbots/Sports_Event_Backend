from django.urls import path
from attending_athletes import views

urlpatterns = [
    path('', views.Attending_athleteList.as_view())
]