from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    auto_now_add=True


    def __str__(self):
        return self.name

