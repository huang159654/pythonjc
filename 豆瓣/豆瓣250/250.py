#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/8/22 22:41
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests

url='https://movie.douban.com/top250?start=25&filter='

response=requests.get(url=url,).text
print(response)