from rest_framework import viewsets
from ..models import Digit
from .serializers import DigitSerializer


class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializer
    queryset = Digit.objects.all()
