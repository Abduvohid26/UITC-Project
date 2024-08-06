from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderView.as_view()),
    path('<uuid:id>/', views.OrderDetailView.as_view()),
    path('address/', views.AddressOrderView.as_view()),
    path('address/<uuid:id>/', views.AddressOrderDetailView.as_view())
]
