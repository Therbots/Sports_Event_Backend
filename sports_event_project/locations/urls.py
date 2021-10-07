from django.urls import path
from locations import views

urlpatterns = [
    path('', views.LocationList.as_view())
]
