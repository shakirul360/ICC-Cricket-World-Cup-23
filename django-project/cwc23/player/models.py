from django.db import models


class Player(models.Model):
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=30)
    total_runs = models.IntegerField()
    total_wickets = models.IntegerField()
    batting_average = models.FloatField()
    bowling_average = models.FloatField(blank=True, null=True)
    recent_match_scores = models.TextField()
    team_name = models.CharField(max_length=30, null=True) 