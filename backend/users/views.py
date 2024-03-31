"""
USER ACCOUNT DJANGO TEMPLATE FROM THIS VIDEO: https://www.youtube.com/watch?v=Z3qTXmT0yoI
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from users.serializers import RegisterSerializer
from users.serializers import RegisterSerializer
from products.models import Purchase

from users.serializers import ChangePasswordSerializer
from django.shortcuts import get_object_or_404

from users.models import CustomUser


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterUserAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class PurchaseHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def format_date(self, date):
        month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]

        return f'{month_names[date.month-1]} {date.day}, {date.year}'

    def get(self, request):
        user = request.user
        purchases = Purchase.objects.filter(user=user)
        response = []
        for purchase in purchases:
            purchase_info = {
                'product': purchase.product.name,
                'product_price': purchase.product.price,
                'company': purchase.product.company,
                'quantity': purchase.quantity,
                'date': self.format_date(purchase.purchase_date.date()),
                'url': purchase.product.url,
                'order_id': purchase.order_id,
                'preview_picture': purchase.product.preview_picture if purchase.product.preview_picture else None
            }

            response.append(purchase_info)

        return Response({
            'purchases': response
        })


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'avatar': 'http://localhost:8000' + user.profile_picture.url if user.profile_picture else None
        })


class ChangePasswordView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)