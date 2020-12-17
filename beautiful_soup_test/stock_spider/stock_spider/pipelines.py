# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StockSpiderPipeline:
    def process_item(self, item, spider):
        return item

class StockPipeline(object):
    # 类被加载时创建一个文件
    def __init__(self):
        # "a+" 文件权限 有-直接写 没有-创建
        self.file = open("executive_prep.csv", "a+")

    def process_item(self, item, spider):
        # 判断文件是否为空
        # 空 + 高管姓名,性别,年龄,股票代码,职位
        # 不为空 + 数据
        if os.path.getsize("executive_prep.csv") > 0:
            # 开始写文件
            self.write_content(item)
        else:
            self.file.write("高管姓名,性别,年龄,股票代码,职位\n")
        # 每次写文件进行刷新
        # 解决判断较慢的问题
        self.file.flush()

        return item

    # 写文件
    def write_content(self, item):
        # 获得数据
        names = item["names"]
        sexes = item["sexes"]
        ages = item["ages"]
        stock_code = item["stock_code"]
        leaders = item["leaders"]

        result = ""
        for i in range(len(names)):
            try:
                result = names[i] + "," + sexes[i] + "," + ages[i]\
                         + "," + stock_code[i] + "," + leaders[i] + "\n"
                self.file.write(result)
            except(IndexError):
                continue