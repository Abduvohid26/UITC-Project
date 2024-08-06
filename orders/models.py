import uuid
from django.db import models
from users.models import User
from foods.models import Food
from django.utils import timezone
PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED = ('pending', 'processing', 'shipped', 'delivered', 'cancelled')


class Order(models.Model):
    ORDER_STATUS = (
        (PENDING, PENDING),
        (PROCESSING, PROCESSING),
        (SHIPPED, SHIPPED),
        (DELIVERED, DELIVERED),
        (CANCELLED, CANCELLED)
    )
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default=PENDING)
    food_qty = models.IntegerField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    person_qty = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.phone_number} by {self.user.username}'


class AddressOrder(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='address_order')
    street = models.CharField(max_length=255)
    dom = models.CharField(max_length=100)
    kvartira = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.street} {self.order.user.full_name}'

