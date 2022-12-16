from django.db import models
from attractions.models import Attractions

# Create your models here.
class TouristHotspot(models.Model):
    name = models.name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)

    def __str__(self):
        return self.nome
