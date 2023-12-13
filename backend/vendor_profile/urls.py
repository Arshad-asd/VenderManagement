from django.urls import path
from purchase_order.views import *
from  vendor_profile.views import *
from vendor_performance.views import VendorPerformanceView

urlpatterns = [
        path('user/register/', UserRegistrationView.as_view(), name='user-registration'),
        path('vendor/register/', VendorRegistrationView.as_view(), name='vemdor-registration'),
        path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # Role based login
        path('vendors/', VendorProfileListCreateView.as_view(), name='vendor-list-create'),
        path('vendors/<int:pk>/', VendorProfileDetailView.as_view(), name='vendor-detail'),
        path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
        path('purchase_orders/<int:pk>/', PurchaseOrderDetailUpdateDeleteView.as_view(), name='purchase-order-detail-update-delete'),
        path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),

]