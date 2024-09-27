from rest_framework.response import Response
from .serializers import signupserialize,loginserialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


# Create your views here.

class signupapi(APIView):
    def post(self, request):
        serializer = signupserialize(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Automatically hashes password and saves the user
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginapi(APIView):
    def post(self, request):
        serializer = loginserialize(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Optionally generate a token if using token-based authentication
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            



