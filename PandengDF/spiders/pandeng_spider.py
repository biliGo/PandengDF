# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午3:39
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : pandeng_spider.py
# @Software: PyCharm
from email import header

import scrapy
from PandengDF.items import PandengItem
import json
import time
import requests


# def books_list():
#     total_count = 238
#     pagesize = total_count
#     url = 'https://api.dushu.io/books'
#     data = {
# 	"bookReadStatus": -1,
# 	"order": 1,
# 	"pageSize": 10,
# 	"token": "qqhQDZLZVRbLM8EOthX",
# 	"page": 1
# }
#
#     res = requests.post(url=url, data=data)
#     print(res.text)


def books_video():
    with open('D:\list\\tt3.json', 'r', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['books']
    lis = []
    for item in ll:
        dic = item['contents']
        for it in dic:
            # it['type'] == 2 音频
            # it['type'] == 3 视频
            if it['type'] == 2:
                if 'fragmentId' in it.keys():
                    lis.append(it['fragmentId'])

    # return lis
    print(lis)


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
                         'Accept': '',
                         'x-dushu-app-ver': '3.9.49'},
                formdata={
                    'token': 'qqhQDZLZVRbLM8EOthX',
                    'fragmentId': str(line)
                },
                callback=self.parse
            )

    def parse(self, response):
        # print('+++++++++++++++', response.text)
        jsobj = json.loads(response.body)
        title = jsobj['title']
        summary = jsobj['summary']
        mediaUrls = jsobj['mediaUrls']

        item = PandengItem()
        item['title'] = title
        item['summary'] = summary
        item['mediaUrls'] = mediaUrls
        yield item
