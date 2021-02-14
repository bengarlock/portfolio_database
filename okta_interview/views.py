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
        url = "https://dev-49794790.okta.com/api/v1/users"
        api_token = return_api_key()

        payload = ""
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'Authorization': 'SSWS' + api_token
        }

        request = requests.request("GET", url, data=payload, headers=headers)
        response = request.json()

        current_django_users = OktaInterview.objects.all()
        current_okta_users = []

        for item in response:
            current_okta_users.append(item["id"])
            first_name = item["profile"]["firstName"]
            last_name = item["profile"]["lastName"]
            mobile = item["profile"]["mobilePhone"]
            display_name = None
            second_email = item["profile"]["secondEmail"]
            login = item["profile"]["login"]
            email = item["profile"]["email"]
            oktaid = item["id"]


            if OktaInterview.objects.filter(oktaid=item["id"]):
                #USER IS FOUND. UPDATE IT.

                print("User {} in database".format(item["id"]))
                user = OktaInterview.objects.get(oktaid=item["id"])
                user.firstName = first_name
                user.lastName = last_name
                user.mobilePhone = mobile
                user.displayName = display_name
                user.secondEmail = second_email
                user.login = login
                user.email = email
                user.save()

            else:
                #USER DOESN'T EXIST IN DJANGO. CREATE IT.
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
        for user in current_django_users:
            #CHECK TO SEE IF USER HAS BEEN DELETED IN OKTA
            if user.oktaid not in current_okta_users:
                dead_user = OktaInterview.objects.get(oktaid=user.oktaid)
                dead_user.delete()

        users = OktaInterview.objects.all()
        return users


