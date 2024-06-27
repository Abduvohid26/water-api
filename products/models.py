from django.db import models
from django.utils import timezone
import uuid
from users.models import phone_regex


class Category(models.Model):
    id = models.URLField(editable=False, primary_key=True, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Product(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name} {self.price}'


NAQT, KARTA = ('naqt', 'karta', )


class Order(models.Model):
    STATUS = (
        (NAQT, NAQT),
        (KARTA, KARTA)
    )
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14, validators=[phone_regex])
    address = models.TextField()
    count = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default=NAQT)

    def __str__(self) -> str:
        return f'{self.product} {self.username}'
