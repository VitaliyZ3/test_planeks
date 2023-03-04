from django.urls import path, re_path

from .views import LoginView, register


urlpatterns = [
    path('' , LoginView.as_view(), name='auth'),
    path('registration/',  register, name='registration')
]

