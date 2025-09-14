from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    mal_id = models.IntegerField(unique=True)
    image_url = models.URLField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title
