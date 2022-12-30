
from warnings import filters
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import TouristHotspot
from .serializers import TouristHotspotSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

class TouristHotspotViewSet(viewsets.ModelViewSet):

    serializer_class = TouristHotspotSerializer
    queryset = TouristHotspot.objects.all()
    filter_backends = [filters.SearchFilter]
    permission_classes = [DjangoModelPermissions,]
    authentication_classes = [TokenAuthentication]
    search_fields = ('name','description')
    
   


   