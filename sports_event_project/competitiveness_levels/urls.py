from django.urls import path
from competitiveness_levels import views

# urlpatterns = [
#     path('', views.Competitiveness_levelList.as_view())
# ]

urlpatterns = [
    path('', views.user_competitiveness_level)
]