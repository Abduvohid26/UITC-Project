from rest_framework import serializers
from .models import Order, AddressOrder
from users.serializers import UserSerializer
from foods.serializers import FoodSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'food', 'food_qty', 'phone_number', 'status', 'name', 'email',
                  'person_qty',  'created_at']


class AddressOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressOrder
        fields = ['id', 'order', 'street', 'dom', 'kvartira', 'comment', 'created_at']


class OrderGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    food = FoodSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'food', 'food_qty', 'phone_number', 'status', 'name', 'email',
                  'person_qty', 'created_at']


class AddressGetOrderSerializer(serializers.ModelSerializer):
    order = OrderGetSerializer()

    class Meta:
        model = AddressOrder
        fields = ['id', 'order', 'street', 'dom', 'kvartira', 'comment', 'created_at']
