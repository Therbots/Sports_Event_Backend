from django.urls import path
from replys import views

urlpatterns = [
    path('', views.ReplyList.as_view())
]
