from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin') 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Role(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    VENDOR = 'vendor', 'Vendor'
    ADMIN = 'admin', 'Admin'
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    vendor_code = models.CharField(max_length=50, unique=True)

    def generate_vendor_code(self):
        # Extract the first three letters of the vendor's name
        name_prefix = slugify(self.name)[:3].upper()

        # Get the last vendor_code to increment
        last_vendor = VendorProfile.objects.order_by('-vendor_code').first()

        if last_vendor:
            last_number = int(last_vendor.vendor_code[3:])
        else:
            last_number = 0

        # Generate a new three-digit number
        new_number = (last_number + 1) % 1000
        new_number_padded = f"{new_number:03d}"

        # Combine the name prefix and the new three-digit number
        new_vendor_code = f"{name_prefix}{new_number_padded}"

        return new_vendor_code

    def save(self, *args, **kwargs):
            if not self.vendor_code:
                self.vendor_code = self.generate_vendor_code()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
