from django.urls import path
from . import views

urlpatterns = [
    path("allAlertas/", views.allAlertas, name="allAlertas"),
    path("loadAlertas/", views.loadAlertas, name="loadAlertas"),
]