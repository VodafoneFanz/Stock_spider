# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import sys
import os

# 调试的写法
# 文件位置
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "tstock"])