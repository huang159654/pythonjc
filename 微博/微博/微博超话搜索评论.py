import csv
import re
from datetime import datetime

import requests
f = open('文章.csv', mode='a', encoding='utf-8—sig', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '博主',
])
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
for page in range(1, 53):
    params = {
        'q': '#贵州村超#',
        'typeall': '1',
        'suball': '1',
        'timescope': 'custom:2023-05-01-0:2023-06-12',
        'Refer': 'g',
        'page': page,
    }

    response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, headers=headers).text
    print(f'正在下载第{page}页')
    response_1 = re.sub('\s', '', response)
    da = re.findall('"@click="copyurl(.*?)"', response_1)
    for url_1 in da:
        url_2 = url_1
        url = url_2.strip("(')")
        id_url = url.split('?')[0].split('/')[-1]  # 文章ID
        essay_id = url.split('/')[3]  # 博主ID
        url_da = id_url = ' https://weibo.com/ajax/statuses/show?id=' + id_url
        list_1 = requests.get(url=url_da, headers=headers, cookies=cookies).json()
        mid_di = list_1['id']  # 文章Id
        oda=str(essay_id)+','+str(mid_di)
        dit = {
            '博主': oda,
        }

        print('下载完毕!', oda)
        csv_writer.writerow(dit)
