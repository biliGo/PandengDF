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


def books_video():
    with open('/Users/guo/PycharmProjects/PandengDF/books_list_fragmentId.json', 'r', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['books']
    lis = []
    for item in ll:
        dic = item['contents']
        for it in dic:
            if it['type'] == 3:
                lis.append(it['fragmentId'])

    return lis
    # print(lis)

class PandengSpider(scrapy.Spider):
    name = 'pandeng'

    # start_urls = [
    #     'http://api.dushu.io/fragment/content'
    # ]
    ll = books_video()



    def start_requests(self):
        url = 'http://api.dushu.io/fragment/content'


        for line in self.ll:

            yield scrapy.FormRequest(
                url=url,
                headers={'Content-Type': 'application/x-www-form-urlencoded',
                         'Accept': ''},
                formdata={
                    'token': '4qWBl9bySjFW9LZBahb',
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