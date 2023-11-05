from django.db import models
class Match(models.Model):
    match_no=models.IntegerField()
    match_team1=models.CharField(max_length=20)
    match_team1_flag=models.CharField(max_length=20)
    match_team2=models.CharField(max_length=20)
    match_team2_flag=models.CharField(max_length=20)
    match_result=models.TextField()
    match_date=models.CharField(max_length=30)
    match_your_time=models.CharField(max_length=15)
    match_local_time=models.CharField(max_length=15)
    match_venue=models.TextField()
    match_highlights=models.TextField()
# Create your models here.