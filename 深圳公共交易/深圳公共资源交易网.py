import re

import requests

response = requests.get('https://old.szggzy.com/jyxx/zfcg',)
# print(response)
sa=response.cookies
fh=response.cookies.get_dict()#获取网页cookies
# print(fh)
acw_tc=fh.get('acw_tc')#字典取值
aliyungf_tc=fh.get('aliyungf_tc')#字典取值

# print(acw_tc)
# print(aliyungf_tc)
cookies = {
    'aliyungf_tc': aliyungf_tc,
    'acw_tc': acw_tc,
    # 'SessionVerify': Session_Verify,
    '.AspNetCore.Antiforgery.99nlv2fL1E0': 'CfDJ8JhznNb8kA1MuZ3iTfqqRUxk_A8ib1rw4k-im42a8SYGNLa-l_-V7xRUeEvdwUoNCfIEqkXJj4BIzWIy-oo-j38IHaUO9Qo-Glx58KOIriOw8_MyjBGEvm-pJUeaCkLJV9tfS0tNKM0R043gdf4_5SE',
    'PowerNodeUniqueVisitor': '2632ff07-1ca6-401a-9ff3-1503a0c99f2d_542_543_544',
    'Power%3A%3ASiteUniqueVisitorKey': '%2F1%2F',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'aliyungf_tc=ad97eedcd09ef5114be2cc7cd70d57d03526fd25177ec1f40551b5ebe0356858; acw_tc=707c9f7016846496665501748e6530e1407b53fb008bdc681c19582012860e; SessionVerify=352d3011-84da-4fad-8df4-4af82d7b1d2e; .AspNetCore.Antiforgery.99nlv2fL1E0=CfDJ8JhznNb8kA1MuZ3iTfqqRUxk_A8ib1rw4k-im42a8SYGNLa-l_-V7xRUeEvdwUoNCfIEqkXJj4BIzWIy-oo-j38IHaUO9Qo-Glx58KOIriOw8_MyjBGEvm-pJUeaCkLJV9tfS0tNKM0R043gdf4_5SE; PowerNodeUniqueVisitor=2632ff07-1ca6-401a-9ff3-1503a0c99f2d_542_543_544; Power%3A%3ASiteUniqueVisitorKey=%2F1%2F',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.get('https://old.szggzy.com/jyxx/zfcg/zbgg_2', cookies=cookies, headers=headers).text
sa_1 = re.findall("<script>window.location.href = '(.*?)';</script>", response)[0]
Session_Verify = sa_1.split('=')[1]
cookies_1 = {
    'aliyungf_tc': aliyungf_tc,
    'acw_tc': acw_tc,
    'SessionVerify': Session_Verify,
    '.AspNetCore.Antiforgery.99nlv2fL1E0': 'CfDJ8JhznNb8kA1MuZ3iTfqqRUxk_A8ib1rw4k-im42a8SYGNLa-l_-V7xRUeEvdwUoNCfIEqkXJj4BIzWIy-oo-j38IHaUO9Qo-Glx58KOIriOw8_MyjBGEvm-pJUeaCkLJV9tfS0tNKM0R043gdf4_5SE',
    'PowerNodeUniqueVisitor': '2632ff07-1ca6-401a-9ff3-1503a0c99f2d_542_543_544',
    'Power%3A%3ASiteUniqueVisitorKey': '%2F1%2F',
}

response_1 = requests.get('https://old.szggzy.com/jyxx/zfcg/zbgg_2', cookies=cookies_1, headers=headers).text
print(response_1)