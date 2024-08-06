from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import OrderSerializer, AddressOrderSerializer, OrderGetSerializer, AddressGetOrderSerializer
from .models import Order, AddressOrder
from rest_framework.response import Response
from rest_framework import status


class OrderView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderGetSerializer(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderGetSerializer(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(instance=order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            order = get_object_or_404(Order, id=id)
        except Exception as e:
            return Response(
                data={
                    'success': False,
                    'message': 'Order not found',
                    'error': f'{e}'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        order.delete()
        return Response(
            data={
                'success': True,
                'message': 'Order successfully deleted'
            }
        )


class AddressOrderView(APIView):
    def get(self, request):
        order = AddressOrder.objects.all()
        serializer = AddressGetOrderSerializer(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddressOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressOrderDetailView(APIView):
    def get(self, request, id):
        order = get_object_or_404(AddressOrder, id=id)
        serializer = AddressGetOrderSerializer(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        order = get_object_or_404(AddressOrder, id=id)
        serializer = AddressOrderSerializer(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        order = get_object_or_404(AddressOrder, id=id)
        serializer = AddressOrderSerializer(data=request.data, instance=order, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            order = get_object_or_404(AddressOrder, id=id)
        except Exception as e:
            return Response(
                data={
                    'success': False,
                    'message': 'AddressOrder not found',
                    'error': f'{e}'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        order.delete()
        return Response(
            data={
                'success': True,
                'message': 'AddressOrder successfully deleted'
            }
        )




