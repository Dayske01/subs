from rest_framework import serializers
from subs import models


# class PersonsSerializer(serializers.Serializer):
#     person = serializers.UUIDField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#
#     def create(self, data):
#         return models.Persons.objects.create(**data)
#
#     def update(self, instance, data):
#         instance.first_name = data.get('first_name', instance.first_name)
#         instance.last_name = data.get('last_name', instance.last_name)
#         instance.save()
#         return instance

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persons
        fields = ['person', 'first_name', 'last_name']
