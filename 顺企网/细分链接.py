#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/8/1 3:21
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""

import re

import pandas
import requests
import parsel

cookies = {
    'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690536714',
    'Hm_lvt_719637f141f1fad6594d68a33b79b0c0': '1690831145',
    'Hm_lpvt_719637f141f1fad6594d68a33b79b0c0': '1690831145',
    'Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690831252',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1690536714; Hm_lvt_719637f141f1fad6594d68a33b79b0c0=1690831145; Hm_lpvt_719637f141f1fad6594d68a33b79b0c0=1690831145; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1690831252',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://product.11467.com/tongyongwujinpeijian/', cookies=cookies, headers=headers).text
x_data=parsel.Selector(response)
div_s=x_data.xpath('//*[@id="il"]/div[1]/div/dl/dd')
i = 1
while True:
    if i < 21:
        for div in div_s:
            neme=div.xpath('.//a/text()').get()
            href = 'https:'+div.xpath('.//a/@href').get()

            print(f'正在下载{i}页,网址{href}')
            url = href + f'pn{i}/'
            i += 1
            cookies1 = {
                'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690536714',
                'Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690555297',
            }

            headers1 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1690536714; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1690555297',
                'Pragma': 'no-cache',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
            response = requests.get(url=url, cookies=cookies1, headers=headers1).text
            name = re.findall('\<div class\=\"btn\-mobile\"\>.*?\<\/div\>\<\/dd\>\<dd\>\<a href\=\".*?"\>(.*?)<\/a\>',
                              response)
            da = re.findall('\<div class\=\"btn\-mobile\"\>(.*?)\<\/div\>', response)  # 电话号码
            # print(da)

            df = pandas.DataFrame({'电话号码': da,
                                   '公司名称': name,
                                   })
            df.to_csv(f'{neme}.csv', mode='a', index=False, encoding='utf_8_sig')
            print(da, name)
    else:
        break
