from rest_framework import viewsets
from core.models import TouristHotspot
from .serializers import TouristHotspotSerializer

class TouristHotspotViewSet(viewsets.ModelViewSet):

    serializer_class = TouristHotspotSerializer

    def get_queryset(self):
        return TouristHotspot.objects.filter(approved=True)