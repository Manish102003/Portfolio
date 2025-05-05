from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    technologies = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
