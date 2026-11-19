from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404

from booking.models import ServiceOffering
from booking.serializers import (
    ServiceOfferingSerializer, 
    ServicesSummarySerializer
    )


class HealthCheckAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "status": "ok",
            "service": "smart-booking"
        })


class ServicesListApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        services = ServiceOffering.objects.filter(is_active=True).order_by("id")

        search_query = request.query_params.get("search")
        if search_query:
            services = services.filter(title__icontains=search_query)

        max_duration_str = request.query_params.get("max_duration")
        if max_duration_str is not None:
            try:
                max_duration = int(max_duration_str)
                services = services.filter(duration_minutes__lte=max_duration)
            except ValueError:
                return Response(
                    {"error": "مقدار max_duration باید یک عدد صحیح معتبر باشد."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        serializer = ServiceOfferingSerializer(services, many=True)

        return Response(serializer.data)


class ServiceDetailAPIView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceOfferingSerializer
    queryset = ServiceOffering.objects.filter(is_active=True)

    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        service.is_active = False
        service.save(update_fields=["is_active"])
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get(self, request, pk):
    #     service = get_object_or_404(
    #         ServiceOffering,
    #         pk=pk,
    #         is_active=True
    #     )
        
    #     serializer = ServiceOfferingSerializer(service)

    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     service = get_object_or_404(ServiceOffering, pk=pk, is_active=True)
    #     service.is_active = False
    #     service.save(update_fields=["is_active"])
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def patch(self, request, pk):
    #     service = get_object_or_404(ServiceOffering, pk=pk, is_active=True)
    #     serializer = ServiceOfferingSerializer(
    #         service, data=request.data, partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class ServicesSummaryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        services = ServiceOffering.objects.filter(
            is_active=True
        ).order_by("id")

        serializer = ServicesSummarySerializer(services, many=True)
        return Response(serializer.data)