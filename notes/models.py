from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    