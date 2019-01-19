from django.db import models

class WebData(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='image')