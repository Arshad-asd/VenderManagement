from django.db import models
from vendor_profile.models import VendorProfile

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"Historical Performance for {self.vendor.name} on {self.date}"
