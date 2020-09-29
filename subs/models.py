""" Описание моделей бд"""

import uuid
from datetime import datetime
from django.db import models


class Groups(models.Model):
    """
    Модель Групп
    """
    group = models.UUIDField(db_column="Group", default=uuid.uuid4, primary_key=True)
    name = models.CharField(db_column="Name", max_length=40)
    description = models.CharField(db_column="Description", max_length=40)
    date_time = models.DateTimeField(db_column="DateTime", default=datetime.now())

    class Meta:
        db_table = "Groups"
        verbose_name = "Группы"
        ordering = ["date_time"]

    def __str__(self):
        return self.name


class Persons(models.Model):
    """
    Модель Персон
    """
    person = models.UUIDField(db_column="Person", default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(db_column="FirstName", max_length=20)
    last_name = models.CharField(db_column="LastName", max_length=20)
    date_time = models.DateTimeField(db_column="DateTime", default=datetime.now())

    class Meta:
        db_table = "Persons"
        verbose_name = "Персоны"
        unique_together = ['first_name', 'last_name']
        ordering = ["date_time"]

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Subscriptions(models.Model):
    """
    Модель Подписок
    """
    subscription = models.UUIDField(db_column="Subscription", default=uuid.uuid4, primary_key=True)
    group = models.ForeignKey(Groups, db_column="Group", on_delete=models.CASCADE)
    person = models.ForeignKey(Persons, db_column="Person", on_delete=models.CASCADE)
    admin = models.BooleanField(db_column="Admin")
    date_time = models.DateTimeField(db_column="DateTime", default=datetime.now())

    class Meta:
        db_table = "Subscriptions"
        verbose_name = "Подписки"
        ordering = ["date_time"]

    def __str__(self):
        return self.subscription
