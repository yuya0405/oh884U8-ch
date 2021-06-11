from django.db import models
from django.utils import timezone

# Create your models here.

class BoardModel(models.Model):
    topic = models.CharField(max_length=30)
    starter = models.CharField(max_length=10)
    replies = models.IntegerField()
    views = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic
