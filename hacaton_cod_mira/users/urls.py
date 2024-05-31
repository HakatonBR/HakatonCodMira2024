from rest_framework import routers
from django.urls import path

from users.views.register import RegisterAPIView
from users.views.login import LoginView
from users.views.logout import LogoutView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]