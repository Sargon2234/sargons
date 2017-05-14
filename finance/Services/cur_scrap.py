from urllib import request
from bs4 import BeautifulSoup


class CurrencyScrapper():
    def __init__(self):
        self.banks = {}

    def main(self, currency: str):
        html = self.__get_html("http://minfin.com.ua/currency/banks/"+ currency)
        self.__parse(html)
        return self.banks

    def __get_html(self, url: str):
        response = request.urlopen(url)
        return response.read()

    def __parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        fullTable = soup.find('table', id='smTable')
        table = fullTable.find('tbody', class_='list')

        for row in table.find_all('tr'):
            cols = row.find_all('td')
            bankName = cols[0].a.text
            buy = cols[1].text
            sell = cols[3].text
            self.banks[bankName] = [buy, sell]
