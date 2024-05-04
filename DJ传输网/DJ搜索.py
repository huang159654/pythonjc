#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/13 17:55
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
import urllib.parse

import requests


class DJ_Search():
    def __init__(self):
        pass
    def def_cookies(self):
        cookies = {
            'PHPSESSID': '0egek4opjr3epb6ao22peba8ub',
            'Dj169_Temporary': '162%2C4590%2C4583%2C4761%2C4788%2C4689%2C',
            'Dj169_history': '162%2C4590%2C4583%2C4761%2C4788%2C4689%2C',
            'openPlayer': '0',
        }
        return cookies
    def def_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=0egek4opjr3epb6ao22peba8ub; Dj169_Temporary=162%2C4590%2C4583%2C4761%2C4788%2C4689%2C; Dj169_history=162%2C4590%2C4583%2C4761%2C4788%2C4689%2C; openPlayer=0',
            'Pragma': 'no-cache',
            'Referer': 'http://www.cnlchl.com/index.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        return headers
    def def_params(self,searchword=None,page=None):
        queries = {
            'page': page,
            'searchword': searchword,
        }
        params = urllib.parse.urlencode(queries)
        return params
    def def_url(self):
        url='http://www.cnlchl.com/search.php'
        return url

    def def_requests(self,searchword=None,page=None):
        response = requests.get(url=self.def_url(), params=self.def_params(searchword=searchword,page=page), cookies=self.def_cookies(), headers=self.def_headers(),
                                verify=False).text
        return response
    def def_parse(self,searchword=None,page=None):
        url_list=re.findall('<h2> <a href="/(.*?)"',self.def_requests(searchword=searchword,page=page))
        for data in url_list:
            url_s='http://www.cnlchl.com/'+data
            yield url_s
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

    def def_requests(self,searchword=None,page=None):
        for url in DJ_Search().def_parse(searchword=searchword,page=page):
            response = requests.get(url=url, cookies=self.dwf_cookies(), headers=self.def_headers(), verify=False).text
            url_mp3 = re.findall('var danceFilePath \= \"(.*?)"\;', response)[0]
            title = re.findall('http://c64-20.djyule.com/.*?/(.*?).mp3', url_mp3)
            video_content = requests.get(url=url_mp3, headers=self.def_headers()).content
            with open('video\\' + str(title) + '.mp4', mode='wb') as f:
                # 写入数据
                f.write(video_content)
            print(f'============下载完毕！{title}============')


if __name__=='__main__':
    # DJ_Search().def_parse()
    searchword=input('请输入搜索的关键词:')
    page_s = int(input('请输入搜索的页数:'))
    for page in range(1,page_s):
        print(f'===================正在采集第{page}页歌曲===================')
        DJ_single().def_requests(searchword=searchword,page=str(page))