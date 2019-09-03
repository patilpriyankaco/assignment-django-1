from django.http import HttpResponse
from django.views import View
from django.core import serializers
import json

from .models import Quote


class QuotesView(View):
    def get(self, request):
        # <view logic>
        quotes = Quote.objects.all()
        return HttpResponse(serializers.serialize('json', quotes))

class QuoteView(View):
    def get(self, request, pk):
        # <view logic>
        quote = Quote.objects.get(id=1)
        quotes = json.loads(serializers.serialize('json', [quote, ]))
        return HttpResponse(json.dumps(quotes[0]))
        # return HttpResponse(pk)


    def post(self, request):
        return HttpResponse('result')