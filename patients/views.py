from rest_framework import serializers, viewsets, status
from .models import Patient
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

# Create your views here.
class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer







