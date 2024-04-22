from django.contrib import admin
from .models import Category, Product, Order

admin.site.register([Category, Product, Order])
