from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
