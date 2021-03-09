from rest_framework import serializers, viewsets, status
from .models import Patient
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


# Create your views here.
class PatientView(viewsets.ViewSet):
    # queryset = Patient.objects.all()
    # serializer_class = PatientSerializer

    def list(self, request):
        print(request.headers)
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def create(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_email = body["data"]["identity"]["claims"]["email"]
        patient = Patient.objects.get(email=user_email)
        ssn = patient.ssn
        member_id = patient.member_id
        medical_records = patient.medical_records
        plan_benefit_info = patient.plan_benefit_info
        prescriptions = patient.prescriptions

        response = {
            "commands": [
                {
                    "type": "com.okta.identity.patch",
                    "value": [
                        {
                            "op": "add",
                            "path": "/claims/extPatientId",
                            "value": ssn,
                        },
                        {
                            "op": "add",
                            "path": "/claims/extPatientId",
                            "value": member_id,
                        },
                        {
                            "op": "add",
                            "path": "/claims/extPatientId",
                            "value": medical_records,
                        },
                        {
                            "op": "add",
                            "path": "/claims/extPatientId",
                            "value": plan_benefit_info,
                        },
                        {
                            "op": "add",
                            "path": "/claims/extPatientId",
                            "value": prescriptions,
                        }
                    ]
                }
            ]
        }

        return Response(response)
