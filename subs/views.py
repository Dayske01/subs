from django.shortcuts import render
from django.http import Http404
from subs import models, serializers
from rest_framework import viewsets


def subs(request, group_id):
    """
    Логика подписок
    :param request: тело запроса
    :param group_id: ид группы
    :return: HttpResponse
    """
    try:
        subscriptions = models.Subscriptions.objects.filter(group=group_id)
    except:
        raise Http404("Нет подписок на группу")

    group = subscriptions[0].group
    admins = [subscription.person for subscription in subscriptions if subscription.admin]
    members = [subscription.person for subscription in subscriptions]
    persons_to_add = models.Persons.objects.all()
    return render(request, 'subs/subs.html', locals())


class PersonsViewSet(viewsets.ModelViewSet):
    """
    API для модели Persons
    """
    serializer_class = serializers.PersonsSerializer
    queryset = models.Persons.objects.all()
