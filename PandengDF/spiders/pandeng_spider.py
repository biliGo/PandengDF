# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午3:39
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : pandeng_spider.py
# @Software: PyCharm

import scrapy
from PandengDF.items import PandengItem
import json
import time


class PandengSpider(scrapy.Spider):
    name = 'pandeng'

    # start_urls = [
    #     'http://api.dushu.io/fragment/content'
    # ]
    ll = [5939, 5842, 5750, 5688, 5645, 5580, 5498, 5431, 5367, 5301, 5242, 5192, 5156, 5121, 5024, 5020, 4992, 4948, 4902, 4842, 4767, 4729, 4657, 4605, 4515, 4479, 4425, 4335, 4306, 4264, 4227, 4195, 4176, 4159, 4124, 4084, 4076, 3947, 3840, 3796, 3716, 3543, 3376, 3345, 3309, 3277, 3244, 3218, 3190, 3167, 3138, 3097, 3059, 3017, 2983, 2943, 2904, 2865, 2827, 2780, 2738, 2705, 2677, 2645, 2609, 2573, 2541, 2503, 2468, 2438, 2376, 2353, 2331, 2305, 2275, 2247, 2212, 2183, 2153, 2126, 2094, 2071, 2042, 2016, 1983, 1955, 1933, 1908, 1889, 1847, 1830, 1809, 1787, 1758, 1735, 1705, 1685, 1656, 1626, 1591, 1572, 1524, 1490, 1454, 1415, 1387, 1360, 1311, 1284, 1256, 1225, 1190, 1166, 1142, 1123, 1077, 1061, 1032, 1014, 988, 953, 943, 902, 882, 849, 820, 790, 774, 744, 729, 710, 688, 665, 648, 621, 605, 594, 518, 503, 551, 440, 406, 368, 351, 425, 287, 269, 250, 317, 186, 146, 122, 218, 231, 121, 88, 87, 84, 1177, 76, 141, 67, 3026, 60, 37, 34, 461, 29, 25, 817, 386, 17, 4, 7, 10, 14]




    def start_requests(self):
        url = 'http://api.dushu.io/fragment/content'


        for line in self.ll:

            yield scrapy.FormRequest(
                url=url,
                headers={'Content-Type': 'application/x-www-form-urlencoded',
                         'Accept': ''},
                formdata={
                    'token': '8faf351735e84895bf8e89b4f2b1d55e',
                    'fragmentId': str(line)
                },
                callback=self.parse
            )




    def parse(self, response):

        jsobj = json.loads(response.body)
        title = jsobj['title']
        summary = jsobj['summary']
        mediaUrls = jsobj['mediaUrls']

        item = PandengItem()
        item['title'] = title
        item['summary'] = summary
        item['mediaUrls'] = mediaUrls
        yield item