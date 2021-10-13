from django.urls import path
from favorite_sports import views

urlpatterns = [
    path('', views.user_favorite_sports)
]