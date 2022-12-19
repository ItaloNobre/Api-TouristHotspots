from rest_framework import viewsets
from core.models import TouristHotspot
from .serializers import TouristHotspotSerializer
class TouristHotspotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TouristHotspot.objects.all()
    serializer_class = TouristHotspotSerializer