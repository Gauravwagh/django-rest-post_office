__author__ = 'gaurav'

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import EmailSerializer
from .models import Email

class EmailViewSet(viewsets.ModelViewSet):
    pass
    queryset = Email.objects.all()
    serializer_class = EmailSerializer