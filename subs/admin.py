from django.contrib import admin
from subs import models


admin.site.register(models.Groups)
admin.site.register(models.Persons)
admin.site.register(models.Subscriptions)
