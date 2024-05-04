#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/9/23 12:07
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import requests

cookies = {
    'sessid': '32AEC56F-50FD-8F2A-9A36-5AA959EE4B4D',
    'aQQ_ajkguid': '163D18EF-56B6-AF3F-FBF2-12D532978785',
    'twe': '2',
    'id58': 'CgAEDWUNcgkHziazDWnJAg==',
    '58tj_uuid': '075e2c02-6eee-48db-b3f2-af96f77dfbdc',
    'init_refer': 'https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.K00000aItsIJV1_TCYhP6vL3YiCEbJqNV4PvGeW98Uj2rLm8qaBelm_qflV9qU1g6EMw7reGkQURzRiFf_Xw8C1m-iZoz9JWcRpedCBiBArCr5RwibPtgIOSSJq3Ng7SwtWMhmC6szn3hJi7DxdFkAEwbbfkyjykXl-3YU3WmPYEocBWbdPpFKv8ILJ8X2MTyDUOHBY7Sds37SlhLt5-LZ_x0yk1.DY_NR2Ar5Od663rj6thm_8jViBjEWXkSUSwMEukmnSrZr1wC4eL_8C5RojPak3S5Zm0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYq_Q2SYeOP0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5UazEVrO1fKzmLmqn0KdThkxpyfqnHRdnWD3nWR1n0KVINqGujYkPHmknHfkrfKVgv-b5HDzP1cdn1f30AdYTAkxpyfqnHc3nWm0TZuxpyfqn0KGuAnqHbC0TA-b5HR0mv-b5HRz0APzm1Ydn16snf%2526dt%253D1695379973%2526wd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526tpl%253Dtpl_12826_33312_0%2526l%253D1552182530%2526ai%253D0_427460369_1_1%2526us%253DlinkVersion%25253D1%252526compPath%25253D10036.0-10032.0%252526label%25253D%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkType%25253D%252526linkText%25253D%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2-%252525E5%252525A5%252525BD%252525E6%25252588%252525BF%252525E5%252525AE%25252589%252525E5%252525BF%25252583%252525E6%2525258C%25252591%25252520%252525E5%25252585%252525A8%252525E5%2525259C%252525A8%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2%252525EF%252525BC%25252581',
    'new_uv': '1',
    '_ga': 'GA1.2.8837361.1695379965',
    '_gid': 'GA1.2.31849278.1695379965',
    'als': '0',
    'new_session': '0',
    '_ga_DYBJHZFBX2': 'GS1.2.1695379965.1.1.1695379978.0.0.0',
    'ajk-appVersion': '',
    'ctid': '121',
    'fzq_h': '68d653179e9ecc385099b607c3f1a43e_1695379994347_7d988140a8e5441ca60a8f59aa23fc25_47901741635336447394054730816051022965',
    'fzq_js_anjuke_ershoufang_pc': '132a83369df1125c621736764ee6296f_1695380018196_23',
    'obtain_by': '1',
    'xxzl_cid': 'a3ea658439224e94822f0c4b5982495e',
    'xxzl_deviceid': '/2v0FK/az91i0qqwYrB7DdW0KrQkKxDbsCiyDNC8IWxkc6ywB3D5963MjMteVoIg',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'sessid=32AEC56F-50FD-8F2A-9A36-5AA959EE4B4D; aQQ_ajkguid=163D18EF-56B6-AF3F-FBF2-12D532978785; twe=2; id58=CgAEDWUNcgkHziazDWnJAg==; 58tj_uuid=075e2c02-6eee-48db-b3f2-af96f77dfbdc; init_refer=https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.K00000aItsIJV1_TCYhP6vL3YiCEbJqNV4PvGeW98Uj2rLm8qaBelm_qflV9qU1g6EMw7reGkQURzRiFf_Xw8C1m-iZoz9JWcRpedCBiBArCr5RwibPtgIOSSJq3Ng7SwtWMhmC6szn3hJi7DxdFkAEwbbfkyjykXl-3YU3WmPYEocBWbdPpFKv8ILJ8X2MTyDUOHBY7Sds37SlhLt5-LZ_x0yk1.DY_NR2Ar5Od663rj6thm_8jViBjEWXkSUSwMEukmnSrZr1wC4eL_8C5RojPak3S5Zm0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYq_Q2SYeOP0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5UazEVrO1fKzmLmqn0KdThkxpyfqnHRdnWD3nWR1n0KVINqGujYkPHmknHfkrfKVgv-b5HDzP1cdn1f30AdYTAkxpyfqnHc3nWm0TZuxpyfqn0KGuAnqHbC0TA-b5HR0mv-b5HRz0APzm1Ydn16snf%2526dt%253D1695379973%2526wd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526tpl%253Dtpl_12826_33312_0%2526l%253D1552182530%2526ai%253D0_427460369_1_1%2526us%253DlinkVersion%25253D1%252526compPath%25253D10036.0-10032.0%252526label%25253D%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkType%25253D%252526linkText%25253D%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2-%252525E5%252525A5%252525BD%252525E6%25252588%252525BF%252525E5%252525AE%25252589%252525E5%252525BF%25252583%252525E6%2525258C%25252591%25252520%252525E5%25252585%252525A8%252525E5%2525259C%252525A8%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2%252525EF%252525BC%25252581; new_uv=1; _ga=GA1.2.8837361.1695379965; _gid=GA1.2.31849278.1695379965; als=0; new_session=0; _ga_DYBJHZFBX2=GS1.2.1695379965.1.1.1695379978.0.0.0; ajk-appVersion=; ctid=121; fzq_h=68d653179e9ecc385099b607c3f1a43e_1695379994347_7d988140a8e5441ca60a8f59aa23fc25_47901741635336447394054730816051022965; fzq_js_anjuke_ershoufang_pc=132a83369df1125c621736764ee6296f_1695380018196_23; obtain_by=1; xxzl_cid=a3ea658439224e94822f0c4b5982495e; xxzl_deviceid=/2v0FK/az91i0qqwYrB7DdW0KrQkKxDbsCiyDNC8IWxkc6ywB3D5963MjMteVoIg',
    'Pragma': 'no-cache',
    'Referer': 'https://anyang.anjuke.com/sale/p2/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://anyang.anjuke.com/sale/p3/', cookies=cookies, headers=headers).text
list_url=re.findall('\<a href\=\"(.*?)" data\-action\=\"esf_list\"',response)
# print(list_url)
for i in list_url:
    text_hxlm=requests.get(url=i,headers=headers,cookies=cookies).text
    title=re.findall('\<title\>(.*?)<\/title\>',text_hxlm)#标题
    name = re.findall('name\=\"keywords\" content\=\"(.*?)\"\>', text_hxlm)  # 名字
    Price = re.findall('is\-contain\=\"true\" alt\=\"(.*?)\"', text_hxlm)  # 价格
    Information = re.findall('\<span class\=\"houseInfo\-main\-item\-name\" data\-v\-991c2cd6\>(.*?)\<\/span\>', text_hxlm)#房源信息
    print(title, name,Price,Information)
    break