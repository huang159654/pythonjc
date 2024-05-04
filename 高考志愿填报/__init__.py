#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/8/12 23:52
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get('http://www.ysygaokao.cn/gxjysjQueryzyjyldetailmulu.aspx?&page=2', headers=headers, verify=False).text
print(response)

da=re.findall('\"onclick\=\"window\.open\(\'\.\.\/cqgxkQuery\.aspx\?YxtsWe\=(.*?)\'\)\"',response)#学校
# print(da)