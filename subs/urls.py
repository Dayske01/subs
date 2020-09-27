from django.urls import path
from subs import views

urlpatterns = [
    path('groups/<uuid:group_id>/', views.subs),
]
