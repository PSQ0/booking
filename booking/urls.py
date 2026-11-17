from django.urls import path

from booking.views import (
    HealthCheckAPIView,
    ServicesListApiView,
    ServiceDetailAPIView,
    ServicesSummaryAPIView,
)

urlpatterns = [
    path("health/", HealthCheckAPIView.as_view(), name="api-health"),
    path("services/", ServicesListApiView.as_view(), name="service-list"),
    path("services/summary/", ServicesSummaryAPIView.as_view(), name="services-summary"),
    path("services/<int:pk>/", ServiceDetailAPIView.as_view(), name="service-detail"),
]