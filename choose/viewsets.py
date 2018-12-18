from rest_framework import viewsets
from .models import Choice
from .serializers import ChoiceSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
