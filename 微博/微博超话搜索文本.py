import csv
import re
from datetime import datetime

import requests
f = open('贵州村超1.csv', mode='a', encoding='utf_8_sig', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '博主',
    '发布时间',
    '文章',
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
    'SSOLoginState': '1686413235',
    'MEIQIA_TRACK_ID': '2Py8D3iO5ERjFy4p4XveSohCCbT',
    'MEIQIA_VISIT_ID': '2R3A29Cd7Tkly2NcIpSSql5H2Ac',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhwgTkwCNuJlRQ.Gkm3_.nk5JpX5KMhUgL.FoMRe0e0ehB0SKB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMpSKqf1hzNS0nN',
    'ALF': '1689091702',
    'SCF': 'Avb4wl1YU4u_AXr9tIYo108FO_5gtW3aBJ9-Q0ZtNbqPP8y5vwqypIjypb-bY2SZuXmlhwkY5hNledsZzbUl-u0.',
    'SUB': '_2A25JgYEnDeRhGeFG6FES8CrPzjiIHXVq9vXvrDV8PUNbmtANLXDAkW9NedHMzJmYukSAQwweam54R_DEkkSRqYYu',
}

headers = {
    'authority': 's.weibo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_s_tentry=weibo.com; Apache=6239456392162.562.1686412727243; SINAGLOBAL=6239456392162.562.1686412727243; ULV=1686412727287:1:1:1:6239456392162.562.1686412727243:; WBtopGlobal_register_version=2023061100; login_sid_t=ef2dbcd046a52fcd92822e09e50d9937; cross_origin_proto=SSL; SSOLoginState=1686413235; MEIQIA_TRACK_ID=2Py8D3iO5ERjFy4p4XveSohCCbT; MEIQIA_VISIT_ID=2R3A29Cd7Tkly2NcIpSSql5H2Ac; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhwgTkwCNuJlRQ.Gkm3_.nk5JpX5KMhUgL.FoMRe0e0ehB0SKB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMpSKqf1hzNS0nN; ALF=1689091702; SCF=Avb4wl1YU4u_AXr9tIYo108FO_5gtW3aBJ9-Q0ZtNbqPP8y5vwqypIjypb-bY2SZuXmlhwkY5hNledsZzbUl-u0.; SUB=_2A25JgYEnDeRhGeFG6FES8CrPzjiIHXVq9vXvrDV8PUNbmtANLXDAkW9NedHMzJmYukSAQwweam54R_DEkkSRqYYu',
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
for page in range(1,8):
    try:
        params = {
            'q': '#贵州村超#',
            'typeall': '1',
            'suball': '1',
            'timescope': 'custom:2023-05-01-0:2023-06-01-0',
            'Refer': 'g',
            'page': page,
        }
        print(f'正在下载第{page}页')
        response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, headers=headers).text
        # print(response)
        response_1 =re.sub('\s','',response)
        da=re.findall('"@click="copyurl(.*?)"',response_1)
        for url_1 in da:
                url_2=url_1
                url=url_2.strip("(')")
                id_url = url.split('?')[0].split('/')[-1]
                params = {
                    'id': id_url,
                }
                response_2 = requests.get('https://weibo.com/ajax/statuses/show', params=params, cookies=cookies,
                                        headers=headers).json()
                print(response_2)
                visible=response_2.get('text_raw',).replace('\n','')#文章
                screen_name = response_2.get('user', ).get('screen_name')#博主
                Comment_time = response_2.get('created_at', )
                d = Comment_time
                created_at = datetime.strptime(d, '%a %b %d %X %z %Y')#发布时间
                dit = {
                    '博主':screen_name,
                    '发布时间':created_at,
                    '文章': visible,
                }

                print('下载完毕!', screen_name,created_at,visible)
                csv_writer.writerow(dit)
    except Exception as e:
        e

