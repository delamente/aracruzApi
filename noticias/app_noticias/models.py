from django.db import models

class Noticia(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()