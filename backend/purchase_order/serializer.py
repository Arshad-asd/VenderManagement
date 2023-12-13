from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
    delivery_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
    issue_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)
    acknowledgment_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
    delivery_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
    issue_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)
    acknowledgment_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)
    promised_date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['po_number', 'vendor']