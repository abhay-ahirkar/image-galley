from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
