"""
URL configuration for decidophobia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import CustomTokenObtainPairView, RegisterUserAPIView, LogoutView, PurchaseHistoryView, ChangePasswordView, ChangeEmailView, ChangeProfilePictureView, UserView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('purchase-history/', PurchaseHistoryView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('change-profile-picture/', ChangeProfilePictureView.as_view(), name='change-profile-picture'),
    path('user/', UserView.as_view())
]
