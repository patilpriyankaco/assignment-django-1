from django.db import models

class Quotes(models.Model):
    quote = models.TextField(max_length=1024)
    author = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=10,decimal_places=2)