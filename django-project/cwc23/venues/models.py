from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    location = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='venue_images/', default='images/img1.jpg')  # Change 'path_to_default_image.jpg' to your default image path
    map_embed_link = models.TextField(blank=True)  # Add this field for embedding the map


    def __str__(self):
        return self.name  + ', ' + self.location
    