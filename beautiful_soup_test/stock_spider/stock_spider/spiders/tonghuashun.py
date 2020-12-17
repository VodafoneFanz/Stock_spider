import scrapy
'''
http://pycs.greedyai.com/
'''

class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/600006/company.html']

    def parse(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[2]/td[1]/a
        # res_selector = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[2]/td[1]/a/text()")
        # name = res_selector.extract()

        # 获得人名字
        tc_names = response.xpath("//*[@class=\"tc name\"]/a/text()").extract()

        for tc_name in tc_names:
            print(tc_name)

        pass
