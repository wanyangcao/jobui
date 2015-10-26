# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:21:22 2015

@author: Administrator
"""

from scrapy.spider import BaseSpider
from scrapy.http import Request
from jobui.items import JobuiItem
from scrapy.selector import Selector
from scrapy.utils.url import urljoin_rfc 

class JobuiSpider(BaseSpider):
    name = "jobui"
    allowed_domains=["jobui.com"]
    start_urls = ["http://www.jobui.com/salary/beijing/"]
    #减慢爬虫速度为1s
    download_delay = 1
    
    
    
    def parse(self, response):
        
        sel = Selector(response)  
        base_url = "http://www.jobui.com" 
        items=[]
        for site in sel.xpath('//*[@id="ui-changeAreaBox"]/ul/li/p/a'):
            item = JobuiItem()
            item['area'] = site.xpath('text()').extract()
            relative_url = site.xpath('@href').extract()[0]
            item['link'] = urljoin_rfc(base_url, relative_url)
            items.append(item)
            
        for item in items:
            yield Request(item['link'], meta={'item':item}, callback=self.parse_item)
            
    def parse_item(self, response):
        sel = Selector(response)
        item = response.meta['item']
        items = []
        item['salary'] = sel.xpath('//*[@id="salary-lenovo"]/div[1]/div/div/div[1]/strong/text()').extract()
        items.append(item)
        return items