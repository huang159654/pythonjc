from datetime import datetime

import requests
q=input('请输入你要搜索的内容:')
cookies = {
    'UOR': 'www.baidu.com,weibo.com,www.baidu.com',
    'SINAGLOBAL': '2649348612320.8965.1683123322503',
    'MEIQIA_TRACK_ID': '2Py8D3iO5ERjFy4p4XveSohCCbT',
    'MEIQIA_VISIT_ID': '2Py8D5U0pLf0VGN2Idzc6ud8scb',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f',
    'XSRF-TOKEN': 'b_h6pP9pINAEpyRJFh--nM-7',
    'SSOLoginState': '1685155264',
    '_s_tentry': 'weibo.com',
    'Apache': '5312540358452.04.1685155351168',
    'ULV': '1685155351206:5:5:1:5312540358452.04.1685155351168:1684412843250',
    'ALF': '1688137017',
    'SCF': 'AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HRXwgWNMo09TKCeFceb2itnjiPwQgl8mrtYsNGz6LGntY.',
    'SUB': '_2A25JcxBsDeRhGeFG6FAZ8ybPyTyIHXVqCQakrDV8PUNbmtANLRHZkW9NedA6PTonwZvM24O5VdWmph6MsVD8dHiG',
    'PC_TOKEN': '0197ee8340',
    'webim_unReadCount': '%7B%22time%22%3A1685613141293%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
    'WBPSESS': 'LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYee1hd8RESfQYZdS7Na4nHW5G3WzC05nXRnLusGg19zo_lqi_nSizThG49tu7RS0wUcF1YAYIpbfacqx3kC6XzN8A==',
}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'client-version': 'v2.40.59',
    # 'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=2649348612320.8965.1683123322503; MEIQIA_TRACK_ID=2Py8D3iO5ERjFy4p4XveSohCCbT; MEIQIA_VISIT_ID=2Py8D5U0pLf0VGN2Idzc6ud8scb; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f; XSRF-TOKEN=b_h6pP9pINAEpyRJFh--nM-7; SSOLoginState=1685155264; _s_tentry=weibo.com; Apache=5312540358452.04.1685155351168; ULV=1685155351206:5:5:1:5312540358452.04.1685155351168:1684412843250; ALF=1688137017; SCF=AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HRXwgWNMo09TKCeFceb2itnjiPwQgl8mrtYsNGz6LGntY.; SUB=_2A25JcxBsDeRhGeFG6FAZ8ybPyTyIHXVqCQakrDV8PUNbmtANLRHZkW9NedA6PTonwZvM24O5VdWmph6MsVD8dHiG; PC_TOKEN=0197ee8340; webim_unReadCount=%7B%22time%22%3A1685613141293%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; WBPSESS=LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYee1hd8RESfQYZdS7Na4nHW5G3WzC05nXRnLusGg19zo_lqi_nSizThG49tu7RS0wUcF1YAYIpbfacqx3kC6XzN8A==',
    'pragma': 'no-cache',
    'referer': 'https://weibo.com/xjb',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.06.01.2',
    'traceparent': '00-72f720937f2d405ecef3b25fd03d6ce7-265368b330bd6e99-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'b_h6pP9pINAEpyRJFh--nM-7',
}

params = {
    'uid': '1784473157',
    'page': '2',
    'feature': '0',
    'q': q,
}

response = requests.get('https://weibo.com/ajax/profile/searchblog', params=params, cookies=cookies, headers=headers).json()
print(response)
#https://weibo.com/1644114654/N22D5gw6n