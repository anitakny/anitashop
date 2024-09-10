from django.db import models

# Create your models here.

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    mood_intensity = models.IntegerField(default=0)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
