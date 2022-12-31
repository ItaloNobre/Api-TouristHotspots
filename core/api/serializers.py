from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import TouristHotspot
from attractions.api.serializers import AttractionSerializer
from comments.api.serializers import CommentSerializer
from assessments.api.serializers import AssessmentSerializer
from addresses.api.serializers import AddressSerializer
from rest_framework import serializers


class TouristHotspotSerializer(ModelSerializer):

    attractions = AttractionSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True,  read_only=True)
    assessments = AssessmentSerializer(many=True , read_only=True)
    addresses = AddressSerializer(read_only=True)
    full_description = serializers.SerializerMethodField()
    
    class Meta:
        model = TouristHotspot
        fields = ['id','name', 'description','approved','attractions','comments','assessments','addresses','full_description','full_description2']
        read_only_fields = ('comments','assessments')

    def get_full_description(self, obj):
        return '%s - %s' %(obj.name, obj.description )