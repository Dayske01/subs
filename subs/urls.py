from django.urls import path
from subs import views


app_name = "subs"
urlpatterns = [
    path('groups/<uuid:group_id>/', views.subs),
    # path('persons/', views.PersonsViewSet.as_view()),
    # path('persons/<uuid:person_id>/', views.PersonsViewSet.as_view())
]
