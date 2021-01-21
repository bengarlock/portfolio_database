from rest_framework import viewsets
from .models import Jobapp
from .serializers import JobappSerializer


class JobappView(viewsets.ModelViewSet):
    queryset = Jobapp.objects.all()
    serializer_class = JobappSerializer
