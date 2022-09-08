from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from data_app.models import UserProfile, UserAddress
from data_app.serializers import UserProfileSerializer, UserAddressSerializer


data_id_model_mapping = {
    "user_profile": {"model": UserProfile, "serializer": UserProfileSerializer},
    "user_address": {"model": UserAddress, "serializer": UserAddressSerializer},
}


class AddData(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    data_id = None

    def post(self, request):
        user = request.user
        data = request.data
        try:
            data_model_serializer = data_id_model_mapping[self.data_id]
        except Exception as e:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # Assigning the user id to the current logged in user
        data["user_id"] = user.user_id

        serializer = data_model_serializer["serializer"](data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetData(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    data_id = None

    def get(self, request):
        # Getting the user
        user = request.user

        try:
            data_model_serializer = data_id_model_mapping[self.data_id]
        except Exception as e:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if self.data_id == "user_profile":
            try:
                # Since user profile is a one to one field, querying using get
                user_profile = data_model_serializer["model"].objects.get(
                    user_id=user.user_id
                )
            except UserProfile.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = data_model_serializer["serializer"](user_profile)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        elif self.data_id == "user_address":
            # Since user address is a multi to one field, querying using filter
            user_addresses = data_model_serializer["model"].objects.filter(
                user_id=user.user_id
            )
            serializer = data_model_serializer["serializer"](user_addresses, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
