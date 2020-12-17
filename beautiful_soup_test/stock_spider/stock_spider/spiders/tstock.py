import scrapy
from urllib import parse
import re
# 导入变量
from stock_spider.items import StockItem


class TstockSpider(scrapy.Spider):
    name = 'tstock'
    allowed_domains = ['pycs.greedyai.com']
    start_urls = ['http://pycs.greedyai.com/']

    def parse(self, response):
        # 定位a标签的href
        post_urls = response.xpath("//a/@href").extract()

        for post_url in post_urls:
            # 域名拼接，回调函数
            yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):
        # 定义变量类
        stock_item = StockItem()

        # 董事会成员姓名
        stock_item["names"] = self.get_tc_names(response)
        # 性别信息
        stock_item["sexes"] = self.get_sex(response)
        # 年龄信息
        stock_item["ages"] = self.get_age(response)
        # 股票代码
        stock_item["stock_code"] = self.get_stock_code(response, len(stock_item["names"]))
        # 职位信息
        stock_item["leaders"] = self.get_leader(response, len(stock_item["names"]))

        # 转交scrapy处理
        yield stock_item

    def get_tc_names(self, response):
        tc_names = response.xpath("//td[@class=\"tc name\"]/a/text()").extract()
        return tc_names

    def get_sex(self, response):
        tc_sexes_init = response.xpath("//td[@class=\"intro\"]/text()").extract()
        # 正则表达式提取性别
        reg = "^[男|女]"
        tc_sexes = []
        for tc_sex in tc_sexes_init:
            try:
                result = re.findall(reg, tc_sex)[0]
                tc_sexes.append(result)
            except(IndexError):
                continue
        return tc_sexes

    def get_age(self, response):
        tc_ages_init = response.xpath("//td[@class=\"intro\"]/text()").extract()
        # 正则表达式提取性别
        reg = "\d+"
        tc_ages = []
        for tc_age in tc_ages_init:
            try:
                result = re.findall(reg, tc_age)[0]
                tc_ages.append(result)
            except(IndexError):
                continue
        return tc_ages

    def get_stock_code(self, response, length):
        infos = response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/h1/a/@title").extract()
        code_list = []
        reg = "\d+"
        code = re.findall(reg, infos[0])[0]
        for i in range(length):
            # code = re.findall(reg, info)[0]
            code_list.append(code)
        return code_list

    def get_leader(self, response, length):
        tc_leaders = response.xpath("//td[@class=\"tl\"]/text()").extract()
        tc_leaders = tc_leaders[:length]
        return tc_leaders
