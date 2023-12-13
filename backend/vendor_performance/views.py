from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializer import VendorPerformanceSerializer

class VendorPerformanceView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VendorPerformanceSerializer
    queryset = HistoricalPerformance.objects.all()

    def get(self, request, *args, **kwargs):
        vendor_id = self.kwargs['vendor_id']
        performances = HistoricalPerformance.objects.filter(vendor__id=vendor_id).order_by('-date')

        if performances.exists():
            latest_performance = performances.first()
            serializer = self.get_serializer(latest_performance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No performance metrics available for this vendor.'}, status=status.HTTP_404_NOT_FOUND)
