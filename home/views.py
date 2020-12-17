from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    queryset = render(request, "index.html", {})
    return render(request, "index.html", {})