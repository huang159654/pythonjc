import re

import requests

cookies = {
    '__trackId': '4195583775013125',
    '__city': 'shanghai',
    'c0fc276cce08ba22dc': 'c858227c49e99b93f0e8cf9226fb4d6d',
    'c1fc276cce08ba22dc': '01b3eb371576396691c038db341c3b5e72c',
    'bxf': '01b3eb371576396691c038db341c3b5e72c',
    'sbxf': '01b3eb371576396691c038db341c3b5e72c',
    'Hm_lvt_5a727f1b4acc5725516637e03b07d3d2': '1687020793',
    'local_flag_guide_shown': '1',
    '__s': '4vk5aius5iinnebekmd9i21nm3',
    '__sense_session_pv': '28',
    'Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2': '1687023623',
}

headers = {
    'authority': 'shanghai.baixing.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__trackId=4195583775013125; __city=shanghai; c0fc276cce08ba22dc=c858227c49e99b93f0e8cf9226fb4d6d; c1fc276cce08ba22dc=01b3eb371576396691c038db341c3b5e72c; bxf=01b3eb371576396691c038db341c3b5e72c; sbxf=01b3eb371576396691c038db341c3b5e72c; Hm_lvt_5a727f1b4acc5725516637e03b07d3d2=1687020793; local_flag_guide_shown=1; __s=4vk5aius5iinnebekmd9i21nm3; __sense_session_pv=28; Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2=1687023623',
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

response = requests.get('https://shanghai.baixing.com/gongzuo/', cookies=cookies, headers=headers).text
url_sa=re.findall("<div class='preview-hover'><a href\=\'(.*?)' ",response)
for url in url_sa:
    id_url=url
    id_data=requests.get(url=id_url,headers=headers,cookies=cookies).text
    print(id_data)
    # Number=re.findall("<strong class='bx-shield-font'>(.*?)</strong>",id_data)#电话号码
    # print(Number)
    # f = {'f': '0', 'F': '1', '1': '2', 'I': '3', 'q': '4', 'i': '5', 'r': '6', '6': '7', 'p': '8', 'c': '9'}
    # do=""
    # for i in Number:
    #     if i == "":
    #         cookies
    #     do += f[i]
    # print(do)
    break