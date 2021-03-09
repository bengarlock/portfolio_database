from rest_framework import serializers, viewsets
from .models import Patient, Prescriptions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = "__all__"


class PrescriptionView(viewsets.ModelViewSet):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionSerializer


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

        ssn = Patient.objects.get(email=user_email).ssn
        member_id = Patient.objects.get(email=user_email).member_id
        medical_records = Patient.objects.get(email=user_email).medical_records
        plan_benefit_info = Patient.objects.get(email=user_email).plan_benefit_info
        prescriptions = Patient.objects.get(email=user_email).prescriptions

        response = {
            "commands": [
                {
                    "type": "com.okta.identity.patch",
                    "value": [
                        {
                            "op": "add",
                            "path": "/claims/ssn",
                            "value": ssn,
                        },
                        {
                            "op": "add",
                            "path": "/claims/memberId",
                            "value": member_id,
                        },
                        {
                            "op": "add",
                            "path": "/claims/medicalRecords",
                            "value": medical_records,
                        },
                        {
                            "op": "add",
                            "path": "/claims/planBenefitInfo",
                            "value": plan_benefit_info,
                        },
                        {
                            "op": "add",
                            "path": "/claims/prescriptions",
                            "value": prescriptions,
                        }
                    ]
                }
            ]
        }

        return Response(response)
