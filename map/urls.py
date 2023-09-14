from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="map-index"),
    path("data", views.data, name="data")
]
