#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/14 13:27
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
import urllib.parse

import requests


class DJ_city():#搜索
    def __init__(self):
        pass
    def def_cookies(self):
        cookies = {
            'Hm_lvt_79e32657a6675f0e9b46c23a8bce03f3': '1707822176',
            'PHPSESSID': '0so0e2pbd8n3mei5r58duqt5ll',
            'adminUrl': 'https%3A%2F%2Fwww.djcscs.com%2Findex.php%3Fac%3Dindex_search%26skey%3D%25E4%25BC%25A4%25E6%2584%259F',
            'Hm_lpvt_79e32657a6675f0e9b46c23a8bce03f3': '1707888323',
        }
        return cookies
    def def_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'Hm_lvt_79e32657a6675f0e9b46c23a8bce03f3=1707822176; PHPSESSID=0so0e2pbd8n3mei5r58duqt5ll; adminUrl=https%3A%2F%2Fwww.djcscs.com%2Findex.php%3Fac%3Dindex_search%26skey%3D%25E4%25BC%25A4%25E6%2584%259F; Hm_lpvt_79e32657a6675f0e9b46c23a8bce03f3=1707888323',
            'Pragma': 'no-cache',
            'Referer': 'https://www.djcscs.com/index.php?ac=index_search&skey=%E4%BC%A4%E6%84%9F',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        return headers

    def def_params(self,page=None):
        queries = {
            'ac': 'index_search',
            'skey': '伤感', #搜索
            'page': page,#页数
        }
        params = urllib.parse.urlencode(queries)
        return params
    def def_url(self):
        url = 'https://www.djcscs.com/index.php'
        return url

    def def_requests(self,page=None):
        response = requests.get(url=self.def_url(), params=self.def_params(page=page), cookies=self.def_cookies(), headers=self.def_headers()).text
        return response
    def def_Parse(self,page=None):
        url_mp3=re.findall('\<a href\=\"(.*?)"  title\=\".*?\"',self.def_requests(page=page))
        for mp3 in url_mp3:
            itle = re.findall('https://www.djcscs.com/play/(.*?).html', mp3)[0]
            dict={'itle':itle}
            # print(dict)
            yield dict
    def def_requests_mp3(self,page=None):
        for def_data in self.def_data(page=page):
            response = requests.post('https://www.djcscs.com/index.php', params=self.def_params_s(), cookies=self.def_cookies(), headers=self.def_headers(), data=def_data).json()
            title=response.get('data').get('title')
            mp3_url = response.get('data').get('mp3')
            video_content = requests.get(url=mp3_url, headers=self.def_headers()).content
            with open('video\\' + str(title) + '.mp3', mode='wb') as f:
                # 写入数据
                f.write(video_content)
            print(f'============下载完毕！{title}============')
    def def_params_s(self):
        params = {
            'ac': 'music_getMusic',
        }
        return params

    def def_data(self,page=None):
        print(page)
        for id in self.def_Parse(page=page):
            data = {
                'id': id['itle'],
            }
            yield data



if __name__=='__main__':
    for page in range(14,37):
        DJ_city().def_requests_mp3(page=page)
    # DJ_city().def_data()