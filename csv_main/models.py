from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TypeRule(models.Model):
    title = models.CharField("Rule title", max_length=32)


class ColumnType(models.Model):
    title = models.CharField("Rule title", max_length=32)
    rule = models.OneToOneField(TypeRule, on_delete=models.SET_NULL, null=True, blank=True)
    # dataset = models.


class Column(models.Model):
    title = models.CharField("Schema title", max_length=32)
    type = models.ForeignKey(ColumnType, on_delete=models.CASCADE)
    order = models.IntegerField()


class Column_separator(models.Model):
    title = models.CharField("Schema title", max_length=32)
    symbol = models.CharField("Char for", max_length=1)


class String_character(models.Model):
    title = models.CharField("Schema title", max_length=32)
    symbol = models.CharField("Char for", max_length=1)


class Schema(models.Model):
    title = models.CharField("Schema title", max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User who created schema")
    column_separator = models.ForeignKey(Column_separator, on_delete=models.SET_NULL, null=True)
    string_character = models.ForeignKey(String_character, on_delete=models.SET_NULL, null=True)
    columns = models.ManyToManyField(Column)
    last_modified = models.DateTimeField(auto_now=True)
