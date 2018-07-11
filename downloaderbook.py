# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 下午3:35
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : downloaderbook.py
# @Software: PyCharm

import os
import requests
import json

def do_load_media(url, path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
        pre_content_length = 0
        # 循环接收视频数据
        while True:
            # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
            if os.path.exists(path):
                headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
            res = requests.get(url, stream=True, headers=headers)

            content_length = int(res.headers['content-length'])
            # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
            if content_length < pre_content_length or (
                    os.path.exists(path) and os.path.getsize(path) == content_length):
                break
            pre_content_length = content_length

            # 写入收到的视频数据
            with open(path, 'ab') as file:
                file.write(res.content)
                file.flush()
                print('receive data，file size : %d   total size:%d' % (os.path.getsize(path), content_length))
    except Exception as e:
        print(e)


def load_media():
    li = []
    with open('/Users/guo/PycharmProjects/PandengDF/pandeng.json', encoding='utf-8') as f:
        li = json.load(f)

    for item in li:
        title = item['title']
        t_left = title.replace('《', '')
        t_right = t_left.replace('》', '')
        summary = item['summary']
        url = item['mediaUrls'][1]

        path = r'/Users/guo/PycharmProjects/PandengDF/media/%s___%s.mp3' % (t_right,summary)
        do_load_media(url, path)
        pass

def load_ysyk():
    with open('/Users/guo/PycharmProjects/PandengDF/6.json', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['data']['contents']
    i = 0
    for item in ll:
        contentTitle = item['contentTitle']
        tit = contentTitle.replace(' ', '')
        title = tit.replace('|', '_')
        audioUrl = item['audioUrl']

        path = r'/Users/guo/PycharmProjects/PandengDF/media/%s.mp3' % title
        do_load_media(audioUrl, path)
        i += 1
        pass
    print('总数:',i,',done!')

def main():
    load_ysyk()
    pass


if __name__ == '__main__':
    main()