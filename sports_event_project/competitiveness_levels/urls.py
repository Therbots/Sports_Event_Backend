from django.urls import path
from competitiveness_levels import views

urlpatterns = [
    path('', views.Competitiveness_levelList.as_view())
]