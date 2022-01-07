from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from config import *


class Question(Item):
    id = Field()
    question = Field()
    # description = Field()


class StackOverFlowSpider(Spider):
    name = 'stackOverFlowSpider'

    custom_settings = {
        'USER_AGENT': USER_AGENT
    }

    start_urls = [URL_SEED_2]

    def parse(self, response):
        sel = Selector(response)
        questions = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        i = 1
        for question in questions:
            item = ItemLoader(Question(), question)
            item.add_xpath('question','.//h3/a/text()')
            # item.add_xpath('description','.//div[@class="excerpt"]/text()')
            item.add_value('id',i)
            i = i + 1
            yield item.load_item()