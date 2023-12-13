from django.db import models
from vendor_profile.models import VendorProfile  


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    promised_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Purchase Order {self.po_number} for {self.vendor.name}"