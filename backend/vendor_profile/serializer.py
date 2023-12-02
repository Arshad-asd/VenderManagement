import re
from vendor_profile.models import Role, VendorProfile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Phone number already exists."),
        ]
    )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True) 

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password', 'password2'] 

    def validate_password(self, password):
        # Password policy: Minimum 6 characters, at least one uppercase letter, one lowercase letter, and one digit
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$', password):
            raise serializers.ValidationError(
                "Password must be at least 6 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."
            )
        return password

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        phone_number = attrs.get('phone_number', None)
        if phone_number:
            # Define a regex pattern for a standard phone number format (adjust as needed)
            phone_number_pattern = r'^\+\d{1,3}-\d{3,14}$'

            # Check if the phone number matches the pattern
            if not re.match(phone_number_pattern, phone_number):
                raise serializers.ValidationError({"phone_number": "Invalid phone number format."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user



class VendorRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Phone number already exists."),
        ]
    )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)  # Add password2 field

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password', 'password2']  # Include password2 field in fields

    def validate_password(self, password):
        # Password policy: Minimum 6 characters, at least one uppercase letter, one lowercase letter, and one digit
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$', password):
            raise serializers.ValidationError(
                "Password must be at least 6 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."
            )
        return password

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        phone_number = attrs.get('phone_number', None)
        if phone_number:
            # Define a regex pattern for a standard phone number format (adjust as needed)
            phone_number_pattern = r'^\+\d{1,3}-\d{3,14}$'

            # Check if the phone number matches the pattern
            if not re.match(phone_number_pattern, phone_number):
                raise serializers.ValidationError({"phone_number": "Invalid phone number format."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role = Role.VENDOR
        )

        user.set_password(validated_data['password'])
         # Mark the user as a tutor
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role 
        token['email'] = user.email
        return token


class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'
        read_only_fields = ['user', 'vendor_code']

    def validate(self, data):
        user = self.context['request'].user
        # Check if a profile already exists for the user
        existing_profile = VendorProfile.objects.filter(user=user).first()
        if existing_profile:
            raise ValidationError("A profile already exists for this user.")
        return data