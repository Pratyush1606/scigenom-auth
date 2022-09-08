from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from auth_app.serializers import UserSerializer


class Signup(APIView):
    """User Signup API"""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(request.data["password"]))
            refresh_token = RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)
            res = {
                "email": str(user),
                "access_token": str(access_token),
                "refresh_token": str(refresh_token),
            }
            return Response(data=res, status=status.HTTP_201_CREATED)
        return Response(
            data={"message": "Data no valid."}, status=status.HTTP_400_BAD_REQUEST
        )
