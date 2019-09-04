from django.http import HttpResponse
from django.views import View
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Quote

class QuotePostView(View):
    @method_decorator(csrf_exempt)
    def post(self, request):
        # <view logic>
        data = request.body.decode('utf-8')
        body = json.loads(data)
        quote = Quote(quote=body["quote"], author=body["author"], rating=body["rating"])
        quote.save()
        return HttpResponse('{"success": true, "id":' + quote.id + "}")


class QuotesView(View):
    def get(self, request):
        # <view logic>
        quotes = Quote.objects.all()
        return HttpResponse(serializers.serialize('json', quotes))

class QuoteView(View):
    def get(self, request, pk):
        # <view logic>
        quote = Quote.objects.get(id=pk)
        quotes = json.loads(serializers.serialize('json', [quote, ]))
        return HttpResponse(json.dumps(quotes[0]))

    @method_decorator(csrf_exempt)
    def delete(self, request, pk):
        Quote.objects.get(id=pk).delete()
        return HttpResponse('{"success": true}')

    @method_decorator(csrf_exempt)
    def put(self, request, pk):
        data = request.body.decode('utf-8')
        body = json.loads(data)
        quote = Quote.objects.get(id=pk)
        quote = Quote(quote=body["quote"], author=body["author"], rating=body["rating"])
        quote.save()
        return HttpResponse('{"success": true}')