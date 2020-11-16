# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapnewsItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    jenis = scrapy.Field()
    judul = scrapy.Field()
    tanggal = scrapy.Field()
    artikel = scrapy.Field()
    pass
