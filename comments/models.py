from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    okay = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
