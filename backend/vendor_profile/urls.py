from django.urls import path

from vendor_profile.views import CustomTokenObtainPairView, UserRegistrationView, VendorProfileCreateView,VendorRegistrationView

urlpatterns = [
        path('user/register/', UserRegistrationView.as_view(), name='user-registration'),
        path('vendor/register/', VendorRegistrationView.as_view(), name='vemdor-registration'),
        path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # Role based login
        path('vendor/create/', VendorProfileCreateView.as_view(), name='vendor-profile-create'),
]