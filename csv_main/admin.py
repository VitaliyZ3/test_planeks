from django.contrib import admin
from . import models

models_to_reg = [
    models.TypeRule,
    models.ColumnType,
    models.Column,
    models.Column_separator,
    models.String_character,
    models.Schema,
]

for model in models_to_reg:
    admin.site.register(model)