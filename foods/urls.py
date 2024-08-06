from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodView.as_view()),
    path('<uuid:id>/', views.FoodDetailView.as_view()),
]
