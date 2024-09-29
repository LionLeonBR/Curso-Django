from django.urls import path
from recipes.views import home, about_us

urlpatterns = [
    path('', home),
    path('about_us/', about_us)
]