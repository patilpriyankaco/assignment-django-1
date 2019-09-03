from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from .crawler import getQuotes
from assignment1.models import Quote
class Command(BaseCommand):
    help = 'Fetch quotes'
    def add_arguments(self, parser):
        parser.add_argument('keyword', nargs='+', type=str, help='Keyword to Search')
        parser.add_argument('length', nargs='+', type=int, help='Number of quotes to fetch')

    def handle(self, *args, **kwargs):
        keyword = kwargs['keyword'][0]
        length = kwargs['length'][0]
        results = getQuotes(keyword, length)
        for result in results:
            quote = Quote(quote=result["quote"], author=result["author"])
            quote.save()
        # print(keyword, length)