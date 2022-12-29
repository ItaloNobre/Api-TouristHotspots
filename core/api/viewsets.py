
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
    filter_backends = [filters.SearchFilter]
    permission_classes = [DjangoModelPermissions,]
    authentication_classes = [TokenAuthentication]
    search_fields = ('name','description')
    
    def get_queryset(self):
          id = self.request.query_params.get('id', None)
          nome = self.request.query_params.get('name', None)
          descricao = self.request.query_params.get('description', None)
          queryset = TouristHotspot.objects.all()

          if id:
               queryset = TouristHotspot.objects.filter(pk=id)

          if nome:
               queryset = queryset.filter(nome__iexact=nome)

          if descricao:
               queryset = queryset.filter(descricao__iexact=descricao)

          return queryset
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
    
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
          pass
    
    @action(methods=['post'], detail=False)
    def teste(self,request):
          pass


   