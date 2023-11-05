from django.db import models
class News(models.Model):
    news_title=models.TextField()
    news_photo=models.TextField()
    news_desc=models.TextField()
# Create your models here.