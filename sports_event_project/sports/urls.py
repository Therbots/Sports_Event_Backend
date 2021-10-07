from django.urls import path
from sports import views

urlpatterns = [
    path('', views.SportList.as_view())
]
