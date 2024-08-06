from django.urls import path
from . import views
urlpatterns = [
    path('', views.UsersView.as_view()),
    path('<uuid:id>/', views.UsersDetail.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('reset-password/', views.ResetPasswordView.as_view())
]
