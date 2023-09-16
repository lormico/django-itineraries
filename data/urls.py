from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'legs', views.LegViewSet)
router.register(r'sidetrips', views.SideTripViewSet)
router.register(r'stays', views.StayViewSet)
router.register(r'websites', views.WebsiteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("reports", views.report, name="reports-index"),
]
