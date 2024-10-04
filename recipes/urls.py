from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('games/<int:id>/', views.game)
]