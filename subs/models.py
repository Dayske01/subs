""" Описание моделей бд"""

import uuid
from django.db import models


class Groups(models.Model):
    """
    Модель Групп
    """
    group = models.UUIDField(db_column="Group", default=uuid.uuid4, primary_key=True)
    name = models.CharField(db_column="Name", max_length=40)
    description = models.CharField(db_column="Description", max_length=40)

    class Meta:
        db_table = "Groups"
        verbose_name = "Группы"


class Persons(models.Model):
    """
    Модель Персон
    """
    person = models.UUIDField(db_column="Person", default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(db_column="FirstName", max_length=20)
    last_name = models.CharField(db_column="LastName", max_length=20)

    class Meta:
        db_table = "Persons"
        verbose_name = "Персоны"


class Subscriptions(models.Model):
    """
    Модель Подписок
    """
    subscription = models.UUIDField(db_column="Subscription", default=uuid.uuid4, primary_key=True)
    group = models.ForeignKey(Groups, db_column="Group", on_delete=models.CASCADE)
    person = models.ForeignKey(Persons, db_column="Person", on_delete=models.CASCADE)
    admin = models.BooleanField(db_column="Admin")

    class Meta:
        db_table = "Subscriptions"
        verbose_name = "Подписки"
