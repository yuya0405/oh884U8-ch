from django.db import models
from django.utils import timezone

# Create your models here.

class BoardModel(models.Model):
    topic = models.CharField(max_length=30)
    starter = models.CharField(max_length=10, default="ๅ็กใ")
    replies = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return str(self.topic)

class PostModel(models.Model):
    topic_id = models.PositiveIntegerField(default=1)
    user = models.CharField(max_length=10)
    posted_date = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return (self.message)
