from rest_framework import viewsets
from attractions.models import Attraction
from .serializers import AttractionSerializer
class AttractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer