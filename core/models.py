from django.db import models
from attractions.models import Attraction
from comments.models import Comment

# Create your models here.
class TouristHotspot(models.Model):
    name = models.name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.nome
