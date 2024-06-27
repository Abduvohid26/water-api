import uuid
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
import random
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
phone_regex = RegexValidator(
    regex=r'^\+998([- ])?(90|91|93|94|95|98|99|33|97|71|88|)([- ])?(\d{3})([- ])?(\d{2})([- ])?(\d{2})$',
    message='Invalid phone number'
)


class Oblast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rayon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=31, unique=False, validators=[phone_regex])
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey(Rayon, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='client', default='profile_pic.jpg',null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    client_id = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f'{self.username} {self.phone_number}'
    

@receiver(post_save, sender=Client)
def send_client_data(sender, instance, created, **kwargs):
    if created:
        message = (f'Yangi Client 📝 \n'
                   f'id: {instance.client_id}\n'
                   f'ism: {instance.username}\n'
                   f'raqami: {instance.phone_number}\n'
                   f'manzil: {instance.region.oblast}, {instance.region}')
        
        telegram_bot_token = "7001254412:AAEqIrIXC2EJhWuyDKcPk1x2BeTmI7YHcWg"
        chat_id = "5700964012"
 
        text_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        text_data = {
            'chat_id': chat_id,
            'text': message,
        }
        requests.post(text_url, data=text_data)

        location_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendLocation"
        location_data = {
            'chat_id': chat_id,
            'latitude': instance.latitude,
            'longitude': instance.longitude,
        }
        requests.post(location_url, data=location_data)
