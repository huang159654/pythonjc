#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/13 17:30
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import requests


#网址：http://www.cnlchl.com/show/4788.html


class DJ_single():
    def __init__(self):
        pass
    def dwf_cookies(self):
        cookies = {
            'PHPSESSID': '0egek4opjr3epb6ao22peba8ub',
            'Dj169_Temporary': '162%2C4590%2C4583%2C4761%2C4788%2C',
            'Dj169_history': '162%2C4590%2C4583%2C4761%2C4788%2C',
            'openPlayer': '1',
        }
        return cookies
    def def_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=0egek4opjr3epb6ao22peba8ub; Dj169_Temporary=162%2C4590%2C4583%2C4761%2C4788%2C; Dj169_history=162%2C4590%2C4583%2C4761%2C4788%2C; openPlayer=1',
            'Pragma': 'no-cache',
            'Referer': 'http://www.cnlchl.com/search.php?searchword=%E4%BC%A4%E6%84%9F',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        return headers

    def def_url(self,url=None):
        url=url
        return url
    def def_requests(self,url=None):
        response = requests.get(url=self.def_url(url=url), cookies=self.dwf_cookies(), headers=self.def_headers(), verify=False).text
        return response
    def def_parse(self,url=None):
        data=self.def_requests(url=url)
        url_mp3=re.findall('var danceFilePath \= \"(.*?)"\;',data)[0]
        return url_mp3
    def def_mp3_url(self,url=None):
        mp3_url=self.def_parse(url=url)
        title=re.findall('http://c64-20.djyule.com/.*?/(.*?).mp3',mp3_url)

        video_content = requests.get(url=mp3_url ,headers=self.def_headers()).content
        with open('video\\' + str(title) + '.mp4', mode='wb') as f:
            # 写入数据
            f.write(video_content)
        print(f'============下载完毕！{title}============')

if __name__=='__main__':
    url=input('请输入你要下载的的歌曲地址-------->>>>')
    DJ_single().def_mp3_url(url=url)