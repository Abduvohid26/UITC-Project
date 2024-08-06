from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import FoodSerializer
from .models import Food
from rest_framework.response import Response
from rest_framework import status


class FoodView(APIView):
    def get(self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(instance=food, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_200_OK)


class FoodDetailView(APIView):
    def get(self, request, id):
        food = get_object_or_404(Food, id=id)
        serializer = FoodSerializer(instance=food)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        food = get_object_or_404(Food, id=id)
        serializer = FoodSerializer(data=request.data, instance=food)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        food = get_object_or_404(Food, id=id)
        serializer = FoodSerializer(data=request.data, instance=food, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            food = get_object_or_404(Food, id=id)
        except Exception as e:
            return Response(
                data={
                    'success': False,
                    'message': 'Fod not found',
                    'error': f'{e}'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        food.delete()
        return Response(
            data={
                'success': True,
                'message': 'Food successfully deleted'
            }
        )


