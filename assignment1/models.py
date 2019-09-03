from django.db import models
from rest_framework import serializers

class Quote(models.Model):
    quote = models.TextField(max_length=1024)
    author = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

# class QuoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quote
#         fields = ["quote", "author", "rating"]