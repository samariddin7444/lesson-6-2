from django.urls import path

from .views import users, about

urlpatterns = [
    path('users/', users),
    path('about/', about),
]