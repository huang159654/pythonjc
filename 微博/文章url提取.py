"""
发布博文的用户昵称 博文发表时间、发布博文文本内容，用户点赞数、用户昵称，和用户评论内容 ，
"""
import csv

import requests
import re
f = open('文章url.csv', mode='a', encoding='utf-8—sig', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '文章url',
])
csv_writer.writeheader()
cookies = {
    '_s_tentry': 'weibo.com',
    'Apache': '6239456392162.562.1686412727243',
    'SINAGLOBAL': '6239456392162.562.1686412727243',
    'ULV': '1686412727287:1:1:1:6239456392162.562.1686412727243:',
    'WBtopGlobal_register_version': '2023061100',
    'login_sid_t': 'ef2dbcd046a52fcd92822e09e50d9937',
    'cross_origin_proto': 'SSL',
    'SUB': '_2A25JgO_jDeRhGeFG6FES8CrPzjiIHXVq9EYrrDV8PUNbmtANLRjHkW9NedHMzAm2D5mMxDOiMQixnWPoyLqLaRc6',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhwgTkwCNuJlRQ.Gkm3_.nk5JpX5o275NHD95QN1he0e05Xe0-XWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNeK-cSKnES0MRS7tt',
    'ALF': '1689005235',
    'SSOLoginState': '1686413235',
    'MEIQIA_TRACK_ID': '2Py8D3iO5ERjFy4p4XveSohCCbT',
    'MEIQIA_VISIT_ID': '2R3A29Cd7Tkly2NcIpSSql5H2Ac',
}

headers = {
    'authority': 's.weibo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_s_tentry=weibo.com; Apache=6239456392162.562.1686412727243; SINAGLOBAL=6239456392162.562.1686412727243; ULV=1686412727287:1:1:1:6239456392162.562.1686412727243:; WBtopGlobal_register_version=2023061100; login_sid_t=ef2dbcd046a52fcd92822e09e50d9937; cross_origin_proto=SSL; SUB=_2A25JgO_jDeRhGeFG6FES8CrPzjiIHXVq9EYrrDV8PUNbmtANLRjHkW9NedHMzAm2D5mMxDOiMQixnWPoyLqLaRc6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhwgTkwCNuJlRQ.Gkm3_.nk5JpX5o275NHD95QN1he0e05Xe0-XWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNeK-cSKnES0MRS7tt; ALF=1689005235; SSOLoginState=1686413235; MEIQIA_TRACK_ID=2Py8D3iO5ERjFy4p4XveSohCCbT; MEIQIA_VISIT_ID=2R3A29Cd7Tkly2NcIpSSql5H2Ac',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
params = {
    'q': 'House事件',
    'xsort': 'hot',
    'Refer': 'hotmore',
}
for i in range(1,100):
    params = {
        'q': '笑果前副总裁评House事件',
        'page': i,
    }

    response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, headers=headers).text
    # response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, ALL_headers=ALL_headers).text
    url_data=re.findall('@click="copyurl(.*?)">',response)
    for url_1 in url_data:
        url_2=url_1
        url=url_2.strip("(')") #去除括号和引号
        dit = {
            '文章url': url,
        }
        print('下载完毕!',url)
        csv_writer.writerow(dit)