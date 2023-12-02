from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from vendor_profile.serializer import CustomTokenObtainPairSerializer, UserRegistrationSerializer, VendorProfileSerializer, VendorRegistrationSerializer
from vendor_profile.models import VendorProfile


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserRegistrationSerializer(user).data, status=status.HTTP_201_CREATED)


class VendorRegistrationView(APIView):
    def post(self, request):
        serializer = VendorRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"message": "Tutor registration successful"}, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class VendorProfileCreateView(generics.CreateAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)