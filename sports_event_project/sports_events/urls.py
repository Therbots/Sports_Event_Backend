from django.urls import path
from sports_events import views

# urlpatterns = [
#     path('', views.Sports_eventList.as_view())
# ]

urlpatterns = [
    path('all/', views.get_all_events),
    path('', views.user_sports_events),
    path('test/', views.Sports_eventList.as_view())
]