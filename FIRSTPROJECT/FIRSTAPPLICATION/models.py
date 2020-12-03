from django.db import models

# Create your models here.

class Candidate(models.Model):
    Name = models.CharField(max_length=20)
    ID = models.CharField(max_length=20)
    Contact = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=20)