from bs4 import BeautifulSoup
import requests


def getStockPrice(stock):
    url = requests.get('https://finance.yahoo.com/quote/'+stock.upper())
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find("fin-streamer", {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    return result.text
