from django.urls import path
from rest_framework.routers import DefaultRouter
from subs import views


app_name = "subs"
urlpatterns = [
    path('groups/<uuid:group_id>/', views.subs),
]

router = DefaultRouter()
router.register(r'api/persons', views.PersonsViewSet, basename='user')
urlpatterns += router.urls
