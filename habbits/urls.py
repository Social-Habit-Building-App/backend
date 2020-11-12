from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import HabbitListCreateView, HabbitDetailView


urlpatterns = [
    path("all-habbits", HabbitListCreateView.as_view(), name="all-habbits"),
    path("habbit/<int:pk>", HabbitDetailView.as_view(), name="habbit"),
]
