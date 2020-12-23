from django.db import models

# Create your models here.

# class Customer(models.Model):
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)



class Blog(models.Model):

    blogname = models.CharField(max_length=500, null=True)
    content = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.blogname