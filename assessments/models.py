from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Assessment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=150,null=True,blank=True)
    punctuation = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
     