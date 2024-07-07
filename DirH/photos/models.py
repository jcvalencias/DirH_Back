from django.db import models

# Create your models here.
class Photo(models.Model):
    image=models.ImageField(upload_to='photos/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    description=models.TextField()

    def __str__(self):
        return self.description