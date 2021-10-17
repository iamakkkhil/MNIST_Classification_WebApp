from .views import DigitViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"digits", DigitViewSet, basename="digits_operations")

urlpatterns = [
    path("", include(router.urls)),
]
