from django.urls import path
from skill_levels import views

# urlpatterns = [
#     path('', views.Skill_levelList.as_view())
# ]

urlpatterns = [
    path('', views.user_skill_level)
]