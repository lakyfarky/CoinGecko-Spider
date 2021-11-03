import scrapy
#source https://www.simplified.guide/scrapy/scrape-table

with open('coins.txt') as f:
    data = f.read().split(',')
    #data = list(reader)
lista=[coin for coin in data]
print(lista[0])
class ScrapeTableSpider(scrapy.Spider):
    name = 'spider1'
 
    def start_requests(self):
        urls = [
            'https://www.coingecko.com/en/coins/{}'.format(c) for c in lista
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        yield {'m_c dominance' : response.xpath('//*[@class="tw-text-gray-900 dark:tw-text-white tw-font-medium"]//text()')[6].extract()}
        # for row in response.xpath('//*[@class="table b-b"]//tbody/tr'):
        #     yield {
        #         'm_c dominance' : row.xpath('td[2]//text()').extract()
        #     }