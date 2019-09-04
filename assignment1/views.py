from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal

import json

from assignment1.models import Quote, QuotesSerializer, QuoteSerializer

class QuotePostView(View):
    @method_decorator(csrf_exempt)
    def post(self, request):
        data = request.body.decode('utf-8')
        body = json.loads(data)
        quote = Quote(**body)
        quote.save()
        resp = {
            "success": True,
            "id": quote.id
        }
        return HttpResponse(json.dumps(resp))


class QuotesView(View):
    def get(self, request):
        # <view logic>
        quotes = QuotesSerializer(Quote.objects.all())
        return HttpResponse(json.dumps(quotes, cls=DecimalEncoder))

class QuoteView(View):
    def get(self, request, pk):
        # <view logic>
        quote = QuoteSerializer(Quote.objects.get(id=pk))
        return HttpResponse(json.dumps(quote, cls=DecimalEncoder))

    @method_decorator(csrf_exempt)
    def delete(self, request, pk):
        Quote.objects.get(id=pk).delete()
        return HttpResponse('{"success": true}')

    @method_decorator(csrf_exempt)
    def put(self, request, pk):
        data = request.body.decode('utf-8')
        body = json.loads(data)
        quote = Quote.objects.get(id=pk)
        for key in body:
            setattr(quote, key, body[key])
        quote.save()
        return HttpResponse('{"success": true}')

    @method_decorator(csrf_exempt)
    def patch(self, request, pk):
        data = request.body.decode('utf-8')
        body = json.loads(data)
        quote = Quote.objects.get(id=pk)
        for key in body:
            setattr(quote, key, body[key])
        quote.save()
        return HttpResponse('{"success": true}')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
