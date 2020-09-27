from django.shortcuts import render
from django.http import Http404
from subs import models


def subs(request, group_id):
    try:
        subscriptions = models.Subscriptions.objects.filter(group=group_id)
    except:
        raise Http404("Нет подписок на группу")

    group = subscriptions[0].group
    admins = [subscription.person for subscription in subscriptions if subscription.admin]
    persons = [subscription.person for subscription in subscriptions]
    return render(request, 'subs/subs.html', locals())
