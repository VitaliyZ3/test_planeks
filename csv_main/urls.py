from django.urls import path

from . import views

urlpatterns = [path("", views.UserDataSchemasView.as_view(), name="main_page")]
