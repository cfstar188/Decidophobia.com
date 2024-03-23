"""
USER ACCOUNT DJANGO TEMPLATE FROM THIS VIDEO: https://www.youtube.com/watch?v=Z3qTXmT0yoI
"""
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegisterSerializer
from products.models import Purchase

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
                'order_id': purchase.order_id
            }

            response.append(purchase_info)

        return Response({
            'purchases': response
        })
