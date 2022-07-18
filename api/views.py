from django.shortcuts import render

# Create your views here.

from .models import Api
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import Apiserializer