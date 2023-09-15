from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="data"),
    path("reports", views.report, name="reports-index"),
]
