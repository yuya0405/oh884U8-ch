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

class Post(models.Model):
    topic = models.CharField(max_length=30)
    user = models.CharField(max_length=10)
    posted_date = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return self.topic
