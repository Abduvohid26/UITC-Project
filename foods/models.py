import uuid
from django.db import models
from django.utils import timezone
PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED = ('pending', 'processing', 'shipped', 'delivered', 'cancelled')


class Food(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='food-images/')
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} {self.price}'
