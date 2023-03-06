from django.urls import path

from .views import LoginView
from .views import logout_user
from .views import register


urlpatterns = [path("login/", LoginView.as_view(), name="login"), path("registration/", register, name="registration"), path("logout/", logout_user, name="logout")]
