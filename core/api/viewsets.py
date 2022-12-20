from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import TouristHotspot
from .serializers import TouristHotspotSerializer

class TouristHotspotViewSet(viewsets.ModelViewSet):

    serializer_class = TouristHotspotSerializer

    def get_queryset(self):
        return TouristHotspot.objects.filter(approved=True)

    def list(self, request, *args, **kwargs):
         return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
         return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
         return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
         return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
         return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
         return super().partial_update(request, *args, **kwargs)
    
    
    