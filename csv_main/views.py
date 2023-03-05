from django.shortcuts import render
from django.views import generic
from .models import Schema

class UserDataSchemas(generic.ListView):
    model = Schema
    template_name = 'csv_main/main_page.html'
    context_object_name = 'user_schemas'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            current_user = self.request.user
            queryset = Schema.objects.filter(user=current_user)
            return queryset
        else:
            return Schema.objects.none()