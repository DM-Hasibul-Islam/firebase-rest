from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.shortcuts import render




class SignupView(APIView):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        try:
            # Extract the data from request
            email = request.data.get('email')
            password = request.data.get('password')
            display_name = request.data.get('display_name')

            # Create user in Firebase
            user = auth.create_user(email=email, password=password, display_name=display_name)

            # Create a user profile in Django database
            user_profile = UserProfile.objects.create(
                user_id=user.uid,
                display_name=display_name,
                email=email
            )
            serializer = UserProfileSerializer(user_profile)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            # Firebase does not have a direct login endpoint, so you would need to
            # handle the login on the frontend or use a third-party package to verify Firebase JWTs.
            return Response({'message': 'Login handled on frontend using Firebase SDK'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
