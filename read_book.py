# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午6:26
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : read_book.py
# @Software: PyCharm
import json
import requests
from bs4 import BeautifulSoup

def loaddata():
    li = []
    data = []
    with open('/Users/guo/PycharmProjects/PandengDF/books.json', encoding='utf-8') as f:
        li = json.load(f)

    for item in li:
        dic = item['contents']
        for dd in dic:
            if dd['type'] == 2:
                data.append(dd['fragmentId'])

    print(data)


def loadysyk():
    with open('/Users/guo/PycharmProjects/PandengDF/6.json', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['data']['contents']

    for item in ll:
        contentTitle = item['contentTitle']
        tit = contentTitle.replace(' ','')
        title = tit.replace('|','_')
        print(title)
        # audioUrl = item['audioUrl']

    # print(dd)
    # print(ll)

def books_video():
    with open('/Users/guo/PycharmProjects/First/books.json', 'r', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['books']
    lis = []
    for item in ll:
        dic = item['contents']
        for it in dic:
            if it['type'] == 3:
                lis.append(it['fragmentId'])

    print(lis)






if __name__ == '__main__':
    loadysyk()