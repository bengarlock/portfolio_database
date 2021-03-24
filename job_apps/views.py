from rest_framework import viewsets, permissions, serializers
from .models import Jobapp


class JobappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobapp
        fields = "__all__"


class JobappView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    queryset = Jobapp.objects.all()
    serializer_class = JobappSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
