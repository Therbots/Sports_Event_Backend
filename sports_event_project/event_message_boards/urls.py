from django.urls import path
from event_message_boards import views

urlpatterns = [
    path('', views.Event_message_boardList.as_view())
]