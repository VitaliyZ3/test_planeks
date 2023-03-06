from django.views import generic

from .models import Schema


class UserDataSchemasView(generic.ListView):
    model = Schema
    template_name = "csv_main/main_page.html"
    context_object_name = "user_schemas"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            current_user = self.request.user
            queryset = Schema.objects.filter(user=current_user).values("title", "last_modified")
            return queryset
        else:
            return Schema.objects.none()


class NewSchemaView(generic.CreateView):
    model = Schema
    template_name = "csv_main/new_schema.html"
    fields = ["title", "last_modified"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
