from django.db import models

# Create your models here.
class Watchlist(models.Model):
    anime_id=models.IntegerField()
    title=models.CharField(max_length=255)
    image_url=models.URLField(max_length=500)
    score=models.FloatField(null=True,blank=True)
    added_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title