from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def index(request):
    return Response({"message": "Hello, world. You're at the test1 index."}, status= status.HTTP_200_OK)

