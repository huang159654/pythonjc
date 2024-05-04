import csv
import time
from datetime import datetime
from pprint import pprint
import random

"""
发布博文的用户昵称 博文发表时间、发布博文文本内容，用户点赞数、用户昵称，和用户评论内容 ，
"""
import requests

f = open('TT评论1.csv', mode='a', encoding='utf-8', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '用户昵称',
    '用户点赞数',
    '用户评论',
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


def get_count(data, uid_data, i=0, next='count=0', ):
    t = len(data)
    while True:  # 这里先把列表长度拿到，然后循环同时一个一个拿取data和uid_data的数据这里是用户id和文章id
        # time.sleep(100)
        url = f'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={data[i]}&is_show_bulletin=2&is_mix=0&{next}&count=20&uid={uid_data[i]}&fetch_level=0'
        print(url)
        response = requests.get(url=url, cookies=cookies, headers=headers).json()
        print(response)
        max_id_0 = response['max_id']  # 这个就是 next,改变这个会有什么变化   我知道要请求，是翻页需要的还是另一个 翻页不需要for循环
        json_data = response.get('data')
        for json in json_data:
            try:
                json_name = json.get('user').get('screen_name')  # 用户名
                json_give = json.get('like_counts')  # 用户点赞
                json_na_me = json.get('text_raw')  # 用户评论
                dit = {
                    '用户昵称': json_name,
                    '用户点赞数': json_give,
                    '用户评论': json_na_me, }
                csv_writer.writerow(dit)
                print('正在下载:',
                      json_name,
                      json_give,
                      json_na_me)
            except Exception as e:
                e
        max_id = 'max_id=' + str(
            max_id_0)  # 这个递归返回
        if max_id_0:
            get_count(data, uid_data, i, max_id)
        else:
            i += 1
            get_count(data, uid_data, i)


if __name__ == '__main__':
    data = [
        '4911499280124595',
        '4911179555937938',
        '4911205157705263',
            ]
    uid_data = [
        '2803301701',
        '2656274875',
        '1887344341',
    ]
    get_count(data=data, uid_data=uid_data)
