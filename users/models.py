import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from client.models import Rayon


phone_regex = RegexValidator(
    regex=r'^\+998([- ])?(90|91|93|94|95|98|99|33|97|71|88|)([- ])?(\d{3})([- ])?(\d{2})([- ])?(\d{2})$',
    message='Invalid phone number'
)

ADMIN, DASTAVCHIK = ('admin', 'dastavchik')


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    USER_ROLES = (
        (ADMIN, ADMIN),
        (DASTAVCHIK, DASTAVCHIK),

    )
    user_roles = models.CharField(max_length=100, choices=USER_ROLES, default=DASTAVCHIK)
    phone_number1 = models.CharField(max_length=14, validators=[phone_regex], unique=False)
    phone_number2 = models.CharField(max_length=14, validators=[phone_regex], null=True, blank=True, unique=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    latitude1 = models.FloatField(null=True, blank=True)
    longitude1 = models.FloatField(null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=3, null=True)


    def __str__(self):
        return self.username

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }

    def save(self, *args, **kwargs):
        self.check_hash_password()
        super(User, self).save(*args, **kwargs)


# class Worker(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     username = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=31, unique=True, validators=[phone_regex])
#     worker_roles = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.username




