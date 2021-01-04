# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import datetime


class HousingPriceSpider(scrapy.Spider):
    name = "zpfdc"

    def start_requests(self):
        urls = ["http://www.zpfdc.com/sale/p1"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for ware_list_item in response.css('div.ware_list_item'):
            yield {
                '链接': ware_list_item.css('div.ware_list_item_2>h3>a::attr(href)').get(),
                '标题': ware_list_item.css('div.ware_list_item_2>h3>a::text').get(),
                '描述1': ware_list_item.css('div.ware_list_item_2>p::text').getall(),
                '更新时间': ware_list_item.css('div.ware_list_item_2>span::text').get(),
                '总价': ware_list_item.css('div.ware_list_item_3>span::text').get(),
                '单价': ware_list_item.css('div.ware_list_item_3>i::text').get()
            }
            last_edit_time = ware_list_item.css('div.ware_list_item_2>span::text').get()
            last_edit_time = last_edit_time.partition('：')[-1].strip()
            if (datetime.datetime.strptime(last_edit_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(
                    days=90)) < datetime.datetime.now():
                return
        next_page = response.css('div.page>a::attr(href)').getall()[-2]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
