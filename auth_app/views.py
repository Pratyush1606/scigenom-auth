from django.urls.base import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.utils import timezone
from auth_app.models import * 
from auth_app.serializers import *

class Hello(APIView):
    '''
    For Welcoming :)
    '''
    def get(self, request):
        data = {
            "query": "Hello World"
        }
        return Response(data=data, status=status.HTTP_200_OK)