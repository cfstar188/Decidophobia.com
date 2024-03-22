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
        print('refreshtoken', request.data.get("refresh_token", ''))
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            print("Token blacklisted")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class PurchaseHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        purchases = Purchase.objects.filter(user=user)
        response = {}
        for index, purchase in enumerate(purchases):
            response[index+1] = {
                'product': purchase.product.name,
                'company': purchase.product.company,
                'quantity': purchase.quantity,
                'date': purchase.purchase_date
            }

        return Response({
            'purchases': response
        })
