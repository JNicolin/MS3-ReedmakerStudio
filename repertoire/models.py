from django.db import models
from reeds.models import Reed

class Repertoire(models.Model):
    music_title = models.CharField(max_length=100, default='add a title')
    music_composer = models.CharField(null=True)
    music_genre = models.CharField(null=True)
    reed = models.ForeignKey(Reed, on_delete=models.SET_NULL, null=True, blank=True, related_name="repertoire_list")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.music_title}, {self.music_composer}"