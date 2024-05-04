#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/9/1 17:50
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'HttpOnly; UM_distinctid=18a5020db63ab8-094d90d4c773c9-26031f51-e1000-18a5020db64897; zh_choose_undefined=s; SERVERID=b2ba659a0bf802d127f2ffc5234eeeba|1693561472|1693561454; CNZZDATA1279942235=1399549459-1693561445-null%7C1693561463; HttpOnly; userGuid=-2001935666; cna=sqB4Hd/5q3cCAf////+10bvT; noOauthRefreshToken=914fc6dc9e348b761281aead6daa8eda; noOauthAccessToken=f9d36258540f9572e6c329ec7c5ac0e8; oauthClientId=demoClient; oauthPath=http://127.0.0.1:8080/EpointWebBuilder; oauthLoginUrl=http://127.0.0.1/membercenter/login.html?redirect_uri=; oauthLogoutUrl=',
    'Origin': 'https://ggzy.zj.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzy.zj.gov.cn/jyxxgk/list.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'token': '',
    'pn': 12,
    'rn': 12,
    'sdt': '',
    'edt': '',
    'wd': '',
    'inc_wd': '',
    'exc_wd': '',
    'fields': 'title',
    'cnum': '001',
    'sort': '{"webdate":"0"}',
    'ssort': 'title',
    'cl': 200,
    'terminal': '',
    'condition': [
        {
            'fieldName': 'categorynum',
            'isLike': True,
            'likeType': 2,
            'equal': '002001001',
        },
        {
            'fieldName': 'infoc',
            'isLike': True,
            'likeType': 2,
            'equal': '33',
        },
    ],
    'time': [
        {
            'fieldName': 'webdate',
            'startTime': '2023-08-29 00:00:00',
            'endTime': '2023-09-01 23:59:59',
        },
    ],
    'highlights': '',
    'statistics': None,
    'unionCondition': None,
    'accuracy': '',
    'noParticiple': '0',
    'searchRange': None,
    'isBusiness': '1',
}

response = requests.post(
    'https://ggzy.zj.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData',
    headers=headers,
    json=json_data,
).json()
print(response)