from django.urls import path
from locations import views

urlpatterns = [
    path('', views.user_location)
]
