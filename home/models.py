from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=30)
    desc = models.TextField()
    def __str__(self):
      return self.name+"-"+self.email