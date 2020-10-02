from rest_framework import serializers
from subs import models


class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persons
        fields = ['person', 'first_name', 'last_name']
