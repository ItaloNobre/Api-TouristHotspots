from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from assessments.models import Assessment

# Create your models here.
class TouristHotspot(models.Model):
    name = models.name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    assessments = models.ManyToManyField(Assessment)

    def __str__(self):
        return self.nome
