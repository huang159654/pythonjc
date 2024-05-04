import csv
from datetime import datetime
from pprint import pprint

"""
发布博文的用户昵称 博文发表时间、发布博文文本内容，用户点赞数、用户昵称，和用户评论内容 ，
"""
import requests

f = open('TT评论2.csv', mode='a', encoding='utf-8', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '博主昵称',
    '发布时间',
    '发布内容',
])
csv_writer.writeheader()
cookies = {
    'UOR': 'www.baidu.com,weibo.com,www.baidu.com',
    'SINAGLOBAL': '2649348612320.8965.1683123322503',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f',
    'XSRF-TOKEN': 'Esh3O_pyGuemuWbImpjxEg_i',
    'SSOLoginState': '1684306503',
    'ALF': '1686985644',
    'SCF': 'AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HR92YdrUEU0AgXTY-y9_cYtik_Qmx4OZgolQ3jofOBljM.',
    'SUB': '_2A25JYb78DeRhGeFG6FAZ8ybPyTyIHXVqFpc0rDV8PUNbmtANLXjQkW9NedA6PQ8S4BZRBkaMXlcfgXMLdFCmNH-z',
    '_s_tentry': 'weibo.com',
    'Apache': '3879985320386.9004.1684412843149',
    'ULV': '1684412843250:4:4:2:3879985320386.9004.1684412843149:1684137851028',
    'MEIQIA_TRACK_ID': '2Py8D3iO5ERjFy4p4XveSohCCbT',
    'MEIQIA_VISIT_ID': '2Py8D5U0pLf0VGN2Idzc6ud8scb',
    'WBPSESS': 'LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYeeD2aNiEHSFkTzLwCJ8eDVyApga2gUpgrRLFtpyO04O4QIlb2g1kLj9YS-oyb2txvWvHjmys8m5R8QjCEGKGXLEA==',
    'UPSTREAM-V-WEIBO-COM': '35846f552801987f8c1e8f7cec0e2230',}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'client-version': 'v2.40.54',
    # 'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=2649348612320.8965.1683123322503; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f; XSRF-TOKEN=Esh3O_pyGuemuWbImpjxEg_i; SSOLoginState=1684306503; ALF=1686985644; SCF=AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HR92YdrUEU0AgXTY-y9_cYtik_Qmx4OZgolQ3jofOBljM.; SUB=_2A25JYb78DeRhGeFG6FAZ8ybPyTyIHXVqFpc0rDV8PUNbmtANLXjQkW9NedA6PQ8S4BZRBkaMXlcfgXMLdFCmNH-z; _s_tentry=weibo.com; Apache=3879985320386.9004.1684412843149; ULV=1684412843250:4:4:2:3879985320386.9004.1684412843149:1684137851028; MEIQIA_TRACK_ID=2Py8D3iO5ERjFy4p4XveSohCCbT; MEIQIA_VISIT_ID=2Py8D5U0pLf0VGN2Idzc6ud8scb; WBPSESS=LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYeeD2aNiEHSFkTzLwCJ8eDVyApga2gUpgrRLFtpyO04O4QIlb2g1kLj9YS-oyb2txvWvHjmys8m5R8QjCEGKGXLEA==',
    'pragma': 'no-cache',
    'referer': 'https://weibo.com/5876465418/N1b8gkNGC',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.05.17.1',
    'traceparent': '00-08a7dd03075c70907ced7376ce3d2a69-928a136104fbfced-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'Esh3O_pyGuemuWbImpjxEg_i',
}
# def Bloggers():

data_1 = ['N0KKyhBmE',
          ]
for id_1 in data_1:
    params = {
        'id': id_1,
    }
    response_Bloggers = requests.get('https://weibo.com/ajax/statuses/show', params=params, cookies=cookies,
                                     headers=headers).json()
    print(response_Bloggers)
    Bloggers_text = response_Bloggers['text_raw'].replace('\n', '')  # 博主发布内容
    Bloggers_name = response_Bloggers.get('user').get('screen_name')  # 博主昵称
    Comment_time = response_Bloggers.get('created_at')  # 发布时间
    d = Comment_time
    Bloggers_time = datetime.strptime(d, '%a %b %d %X %z %Y')  # 发布时间
    print(Bloggers_name, Bloggers_time, )
    dit = {
        '博主昵称': Bloggers_name,
        '发布时间': Bloggers_time,
        '发布内容':Bloggers_text,

    }
    csv_writer.writerow(dit)
