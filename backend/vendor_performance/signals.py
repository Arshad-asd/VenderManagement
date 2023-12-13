# vendor_performance/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F, Count, Avg, ExpressionWrapper, fields
from django.db.models.functions import Coalesce
from django.utils import timezone
from purchase_order.models import PurchaseOrder
from .models import HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        date = timezone.now()

        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        quality_rating_avg = calculate_quality_rating_avg(vendor)
        average_response_time = calculate_average_response_time(vendor)
        fulfillment_rate = calculate_fulfillment_rate(vendor)

        historical_performance, created = HistoricalPerformance.objects.get_or_create(
            vendor=vendor,
            date=date,
            defaults={
                'on_time_delivery_rate': on_time_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': average_response_time,
                'fulfillment_rate': fulfillment_rate,
            }
        )

        if not created:
            historical_performance.on_time_delivery_rate = on_time_delivery_rate
            historical_performance.quality_rating_avg = quality_rating_avg
            historical_performance.average_response_time = average_response_time
            historical_performance.fulfillment_rate = fulfillment_rate
            historical_performance.save()

def calculate_on_time_delivery_rate(vendor):
    total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

    if total_completed_orders == 0:
        return 0.0

    on_time_deliveries = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        delivery_date__lte=F('promised_date')
    ).count()

    on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100.0

    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor):
    quality_rating_avg = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        quality_rating__isnull=False
    ).aggregate(average_quality=Avg('quality_rating'))['average_quality'] or 0.0

    return quality_rating_avg

def calculate_average_response_time(vendor):
    avg_response_time = PurchaseOrder.objects.filter(
        vendor=vendor,
        acknowledgment_date__isnull=False
    ).annotate(
        response_time=ExpressionWrapper(
            F('acknowledgment_date') - F('issue_date'),
            output_field=fields.DurationField()
        )
    ).aggregate(average_response_time=Coalesce(Avg('response_time'), timezone.timedelta(0)))['average_response_time']

    avg_response_time_seconds = avg_response_time.total_seconds() if avg_response_time else 0.0

    return avg_response_time_seconds

def calculate_fulfillment_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()

    if total_orders == 0:
        return 0.0

    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', issue_date__isnull=True).count()

    fulfillment_rate = (fulfilled_orders / total_orders) * 100.0

    return fulfillment_rate
