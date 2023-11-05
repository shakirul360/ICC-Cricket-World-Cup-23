from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    flag = models.ImageField(upload_to='venue_images/', default='images/img1.jpg')  # Change 'path_to_default_image.jpg' to your default image path
    
    