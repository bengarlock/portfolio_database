from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import OktaInterview
import requests
from passwords import return_api_key
from rest_framework.views import APIView
from rest_framework.response import Response



def sync_okta():
    url = "https://dev-49794790.okta.com/api/v1/users"
    api_token = return_api_key()

    payload = ""
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': 'SSWS' + api_token
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    response_json = response.json()
    return response.json()

    for item in response_json:
        if OktaInterview.objects.filter(oktaid=item["id"]):
            print("User {} in database".format(item["id"]))

        else:
            first_name = item["profile"]["firstName"]
            last_name = item["profile"]["lastName"]
            mobile = item["profile"]["mobilePhone"]
            display_name = None
            second_email = item["profile"]["secondEmail"]
            login = item["profile"]["login"]
            email = item["profile"]["email"]
            oktaid = item["id"]

            OktaInterview.objects.create(
                firstName=first_name,
                lastName=last_name,
                mobilePhone=mobile,
                displayName=display_name,
                secondEmail=second_email,
                login=login,
                email=email,
                oktaid=oktaid,
            )


class OktaInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        sync_okta()
        model = OktaInterview
        fields = "__all__"


# Create your views here.
class OktaInterviewView(viewsets.ModelViewSet):
    queryset = OktaInterview.objects.all()
    serializer_class = OktaInterviewSerializer

    def get_queryset(request, format=None):
        users = OktaInterview.objects.all()
        return users


