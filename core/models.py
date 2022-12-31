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
    addresses = models.ForeignKey(
        Address, on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def full_description2(self):
        return '%s - %s' %(self.name, self.description )

    def __str__(self):
        return self.name
