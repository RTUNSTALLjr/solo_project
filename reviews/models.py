from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=255)
    score = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    score = models.IntegerField()
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Upcoming(models.Model):
    pass