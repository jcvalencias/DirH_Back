from django.db import models

# Create your models here.
class Photo(models.Model):
    image=models.ImageField(upload_to='photos/')
    location=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.description