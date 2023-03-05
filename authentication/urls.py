from django.urls import path, re_path

from .views import LoginView, register, logout_user


urlpatterns = [
    path('login/' , LoginView.as_view(), name='login'),
    path('registration/',  register, name='registration'),
    path('logout/', logout_user, name='logout')
]

