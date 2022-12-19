from rest_framework.serializers import ModelSerializer
from core.models import TouristHotspot


class TouristHotspotSerializer(ModelSerializer):
    class Meta:
        model = TouristHotspot
        fields = ['id','name', 'description']