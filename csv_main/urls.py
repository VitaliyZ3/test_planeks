from django.urls import path, re_path
from . import views 
urlpatterns = [
    path('', views.UserDataSchemas.as_view(), name='main_page')
]