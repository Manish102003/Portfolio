from django.db import models

# Create your models here.
class Experience(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    certificate = models.FileField(upload_to='certificate/',null=True,)
    def __str__(self):
        return self.name