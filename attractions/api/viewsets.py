from rest_framework import viewsets
from attractions.models import Attraction
from .serializers import AttractionSerializer
from rest_framework import filters
class AttractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name','^description')
    """lookup_field = 'name'"""