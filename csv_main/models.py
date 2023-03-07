from django.contrib.auth.models import User
from django.db import models


class TypeRule(models.Model):
    title = models.CharField("Rule title", max_length=32)
    from_value = models.CharField("From", max_length=32)
    to_value = models.CharField("To", max_length=32)


class ColumnType(models.Model):
    title = models.CharField("Rule title", max_length=32)
    extra_arguments = models.OneToOneField(TypeRule, on_delete=models.SET_NULL, null=True, blank=True)
    # dataset = models.


class Column(models.Model):
    title = models.CharField("Schema title", max_length=32)
    type = models.ForeignKey(ColumnType, on_delete=models.CASCADE)
    order = models.IntegerField()


class ColumnSeparator(models.Model):
    title = models.CharField("Schema title", max_length=32)
    symbol = models.CharField("Char for", max_length=1)


class StringCharacter(models.Model):
    title = models.CharField("Schema title", max_length=32)
    symbol = models.CharField("Char for", max_length=1)


class Schema(models.Model):
    title = models.CharField("Schema title", max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User who created schema")
    column_separator = models.ForeignKey(ColumnSeparator, on_delete=models.SET_NULL, null=True)
    string_character = models.ForeignKey(StringCharacter, on_delete=models.SET_NULL, null=True)
    columns = models.ManyToManyField(Column)
    last_modified = models.DateTimeField(auto_now=True)


class GeneratedCVS(models.Model):
    STATUS_CHOICES = (
        (1, "Processing"),
        (2, "Ready"),
    )
    created_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    file_scr = models.FileField(upload_to="")
