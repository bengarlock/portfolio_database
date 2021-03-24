from rest_framework import serializers
from .models import Jobapp


class JobappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobapp
        fields = "__all__"
