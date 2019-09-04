from django.db import models

class Quote(models.Model):
    quote = models.TextField(max_length=1024)
    author = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

def QuoteSerializer(obj):
    fields = ['id', 'quote', 'author', 'rating']
    return {val: getattr(obj, val) for val in fields}
    
def QuotesSerializer(objs):
    return [QuoteSerializer(obj) for obj in objs]