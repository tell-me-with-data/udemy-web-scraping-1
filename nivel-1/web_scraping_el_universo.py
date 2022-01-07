from config import *
from bs4 import BeautifulSoup
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class New(Item):
    id = Field()
    header = Field()
    description = Field()


class ElUniversoSpider(Spider):
    name = 'elUniversoSpider'
    i = 1
    custom_settings = {
        'USER_AGENT': USER_AGENT
    }

    start_urls = [URL_SEED_3]

    def parse(self, response):
        i = 1
        soup = BeautifulSoup(response.body)
        news = soup.find_all('li', class_="relative")
        for new in news:
            item = ItemLoader(New(), response.body)
            item.add_value('id', i)
            item.add_value('header',new.find('a', class_='no-underline').text)
            item.add_value('description',new.find('p').text)
            i = i + 1
            yield item.load_item()      
        # Scrapy Way
        # i = 1
        # sel = Selector(response)
        # news = sel.xpath('//div[contains(@class,"results")]//li[contains(@class,"relative")]')
        # for new in news:
        #     item = ItemLoader(New(), new)
        #     item.add_xpath('header','.//a[@class="no-underline"]/text()')
        #     item.add_xpath('description','.//p[contains(@class,"summary")]/text()')
        #     item.add_value('id', i)
        #     i = i + 1
        #     yield item.load_item()
