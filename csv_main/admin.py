from django.contrib import admin

from . import models

models_to_reg = [
    models.TypeRule,
    models.ColumnType,
    models.Column,
    models.ColumnSeparator,
    models.StringCharacter,
    models.GeneratedCVS,
    models.Schema,
]

for model in models_to_reg:
    admin.site.register(model)
