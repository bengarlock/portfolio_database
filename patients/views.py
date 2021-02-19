from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Patients
import requests
from passwords import return_api_key
from rest_framework.views import APIView
from rest_framework.response import Response



class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"


# Create your views here.
class PatientsView(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer



