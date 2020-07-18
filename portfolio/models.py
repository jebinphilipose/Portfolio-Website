from django.db import models
from django.utils import timezone


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    github_link = models.URLField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
