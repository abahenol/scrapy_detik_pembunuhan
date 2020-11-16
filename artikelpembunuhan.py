# Spider 2
# ArticleScraper.py which scrape article headlies and bodies
# imports
import scrapy
from scrapy.http import Request
from ..items import ScrapnewsItem
import json

class ArticlescraperSpider(scrapy.Spider):
    name = 'artikelpembunuhan'
    allowed_domains = ['detik.com']
    start_urls = ['https://www.detik.com/search/searchall?query=pembunuhan&siteid=2&sortby=time&page=1']

    def start_requests(self):
        # Open the JSON file which contains article links
        with open('/Users/Salim Satriajati/Documents/Semnas Offstat 2020/newsscraper/scrapnews/linkpembunuhanfix.json') as json_file:
            data = json.load(json_file)
    
        for p in data:
            print('URL: ' + p['link'])
        
            request = Request(p['link'],callback=self.parse_article_page)
            yield request
    
    def parse_article_page(self,response):
        items = ScrapnewsItem()
        items['jenis']='pembunuhan'
        items['link'] = response.request.url 
        items['judul']=response.css('h1.detail__title::text').extract()
        items['tanggal']=response.css('.detail__date::text').extract()
        items['artikel']= response.css('.detail__body-text *::text').extract()

        items['artikel'] = ''.join(items['artikel'])
        items['judul'] = ''.join(items['judul'])
        items['tanggal'] = ''.join(items['tanggal'])
        
        items['judul'] = items['judul'].replace('\n','').strip()
        items['artikel'] = items['artikel'].replace('\n','').replace('\r','').strip()[0:500]
        yield items

    def parse(self, response):
        pass