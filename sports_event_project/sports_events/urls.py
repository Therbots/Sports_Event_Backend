from django.urls import path
from sports_events import views

urlpatterns = [
    path('', views.Sports_eventList.as_view())
]