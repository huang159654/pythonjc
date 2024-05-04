import time
import requests

#日期转换为时间戳
print('输入日期格式 2323-2-3')
da = input('请输入日期:')
dada=da +' 00:00:00'
# print(dada)
s_t = time.strptime(dada, "%Y-%m-%d %H:%M:%S")  # 返回元祖
mkt = int(time.mktime(s_t))


cookies = {
    'UOR': 'www.baidu.com,weibo.com,www.baidu.com',
    'SINAGLOBAL': '2649348612320.8965.1683123322503',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f',
    'XSRF-TOKEN': 'IU0Ju8kPvYL1IjikjkNn1KqI',
    'ALF': '1686726821',
    'SSOLoginState': '1684134821',
    'SCF': 'AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HR2E-GuQ8NitkUlwml_oLklZMGxhOT47lJOdb0epKaEqM.',
    'SUB': '_2A25JZav1DeRhGeFG6FAZ8ybPyTyIHXVqEpo9rDV8PUNbmtANLWj3kW9NedA6PUW_bDy_R7HXbE1wTPigj4bTMdoU',
    '_s_tentry': 'www.baidu.com',
    'Apache': '6238390337761.372.1684137850994',
    'ULV': '1684137851028:3:3:1:6238390337761.372.1684137850994:1683377818731',
    'webim_unReadCount': '%7B%22time%22%3A1684137851608%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
    'WBPSESS': 'LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYee1hd8RESfQYZdS7Na4nHW5PtedMiHe7SuTHY_8ttzshXzFUyJGS5rz7gLYC9jD-3Vj3l3TW9K6VbbSPox04cHPQ==',
}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'client-version': 'v2.40.50',
    # 'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=2649348612320.8965.1683123322503; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f; XSRF-TOKEN=IU0Ju8kPvYL1IjikjkNn1KqI; ALF=1686726821; SSOLoginState=1684134821; SCF=AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HR2E-GuQ8NitkUlwml_oLklZMGxhOT47lJOdb0epKaEqM.; SUB=_2A25JZav1DeRhGeFG6FAZ8ybPyTyIHXVqEpo9rDV8PUNbmtANLWj3kW9NedA6PUW_bDy_R7HXbE1wTPigj4bTMdoU; _s_tentry=www.baidu.com; Apache=6238390337761.372.1684137850994; ULV=1684137851028:3:3:1:6238390337761.372.1684137850994:1683377818731; webim_unReadCount=%7B%22time%22%3A1684137851608%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; WBPSESS=LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYee1hd8RESfQYZdS7Na4nHW5PtedMiHe7SuTHY_8ttzshXzFUyJGS5rz7gLYC9jD-3Vj3l3TW9K6VbbSPox04cHPQ==',
    'pragma': 'no-cache',
    'referer': 'https://weibo.com/u/5530682472',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.05.11.1',
    'traceparent': '00-f28a25d3f5bdf46e4e5e336279b2bba2-ca6426590e148c24-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'IU0Ju8kPvYL1IjikjkNn1KqI',
}

params = {
    'uid': '5530682472',
    'page': '1',
    'feature': '4',
    'starttime': mkt,
    'endtime': '1683216000',
}

response = requests.get('https://weibo.com/ajax/statuses/searchProfile', params=params, cookies=cookies, headers=headers).json()
print(response)