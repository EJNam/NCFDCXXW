import scrapy
from planning.items import PlanningItem

class PlSpider(scrapy.Spider):
    name = 'pl'
    #allowed_domains = ['http://zrzy.jiangsu.gov.cn']
    start_urls = ['http://zrzy.jiangsu.gov.cn/gtapp/xxgk/tdsc_getGdxmList.action?xzqhdm=320500']

    
        
    def parse(self, response):
        url = response.url
        res = response.xpath('//a/@href').getall()
        for url in res[:]:
            url = 'http://zrzy.jiangsu.gov.cn/gtapp/xxgk/' + url.replace('\\"','')
            yield scrapy.Request(url, callback=self.parse_table)
            
    def parse_table(self, response):
        item = PlanningItem()
        item['XZQM'] = response.xpath('//*[(@id = "XZQ_DM")]/text()').get()
        item['XMMC'] = response.xpath('//*[(@id = "XM_MC")]/text()').get()
        item['FQZFYD'] = response.xpath('//*[(@id = "div_crj")]//td//text()').get()
        return item
