from django.urls import path
from favorite_sports import views

urlpatterns = [
    path('', views.Favorite_sportList.as_view())
]