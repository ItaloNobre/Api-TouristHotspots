from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from assessments.models import Assessment
from addresses.models import Address

# Create your models here.
class TouristHotspot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction,null=True,blank=True)
    comments = models.ManyToManyField(Comment,null=True,blank=True)
    assessments = models.ManyToManyField(Assessment,null=True,blank=True)
    Addresses = models.ForeignKey(
        Address, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.name
