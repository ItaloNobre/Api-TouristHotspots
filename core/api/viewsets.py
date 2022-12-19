from rest_framework import viewsets
from core.models import TouristHotspot
from .serializers import TouristHotspotSerializer

class TouristHotspotViewSet(viewsets.ModelViewSet):
   
    queryset = TouristHotspot.objects.all()
    serializer_class = TouristHotspotSerializer