from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailObtainTokenPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.validated_data, status=status.HTTP_200_OK)

class EmailObtainTokenPairView(TokenObtainPairView):
    serializer_class = EmailObtainTokenPairSerializer