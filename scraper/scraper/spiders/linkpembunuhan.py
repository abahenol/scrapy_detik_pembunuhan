import scrapy
from ..items import ScrapnewsItem


class PembunuhanSpider(scrapy.Spider):
    name = 'linkpembunuhan'
    page_number = 2
    start_urls = ['https://www.detik.com/search/searchall?query=pembunuhan&siteid=2&sortby=time&page=1']

    def parse(self, response):
        items = ScrapnewsItem()
        news = response.css('article')

        for text in news:
            #judul = text.css('h2.title::text').extract_first()
            #tanggal = text.css('span.date::text').extract_first()
            link = text.css('a::attr(href)').extract_first()
            
            #items['judul'] = judul
            #items['tanggal'] = tanggal
            items['link'] = link

            yield items
        
        next_page = 'https://www.detik.com/search/searchall?query=pembunuhan&siteid=2&sortby=time&page='+str(PembunuhanSpider.page_number)+'/'
        if PembunuhanSpider.page_number <= 3:
            PembunuhanSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)