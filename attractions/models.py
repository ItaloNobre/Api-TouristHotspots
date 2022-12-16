from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    minimum_age = models.IntegerField()

    def __str__(self):
        return self.nome