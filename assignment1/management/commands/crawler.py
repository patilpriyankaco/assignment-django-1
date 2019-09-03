from urllib.request import urlopen
from bs4 import BeautifulSoup

def getQuotes(keyword, length):
    url = 'https://www.goodreads.com/quotes/search?q=' + keyword
    data = urlopen(url)
    soup = BeautifulSoup(data.read(), 'html.parser')
    [x.extract() for x in soup.findAll('script')]
    quotes = soup.find_all('div', class_="quoteDetails")
    # print(quotes)
    results = []
    for quote in quotes[:length]:
        quoteEl = quote.find(class_='quoteText')
        authorEl = quoteEl.find(class_='authorOrTitle')
        author = authorEl.get_text().strip()
        authorEl.extract()
        quoteText = quoteEl.get_text().strip()
        results.append({
            "quote": quoteText,
            "author": author
        })
    return results
    # print(results)