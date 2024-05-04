import json
import re

import requests

cookies = {
    'ba17301551dcbaf9_gdp_user_key': '',
    'gdp_user_id': 'gioenc-24d7837e%2C37e0%2C54d2%2Ccc1a%2C2g384dg01e29',
    'ba17301551dcbaf9_gdp_session_id_69aa7da9-3e4b-48c9-9322-f3a62f05cac5': 'true',
    'ba17301551dcbaf9_gdp_session_id': 'f34779af-8950-4168-8e81-7d6bd6c56a08',
    'ba17301551dcbaf9_gdp_session_id_f34779af-8950-4168-8e81-7d6bd6c56a08': 'true',
    'ba17301551dcbaf9_gdp_sequence_ids': '{%22globalKey%22:60%2C%22VISIT%22:3%2C%22PAGE%22:8%2C%22VIEW_CLICK%22:42%2C%22CUSTOM%22:10}',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'ba17301551dcbaf9_gdp_user_key=; gdp_user_id=gioenc-24d7837e%2C37e0%2C54d2%2Ccc1a%2C2g384dg01e29; ba17301551dcbaf9_gdp_session_id_69aa7da9-3e4b-48c9-9322-f3a62f05cac5=true; ba17301551dcbaf9_gdp_session_id=f34779af-8950-4168-8e81-7d6bd6c56a08; ba17301551dcbaf9_gdp_session_id_f34779af-8950-4168-8e81-7d6bd6c56a08=true; ba17301551dcbaf9_gdp_sequence_ids={%22globalKey%22:60%2C%22VISIT%22:3%2C%22PAGE%22:8%2C%22VIEW_CLICK%22:42%2C%22CUSTOM%22:10}',
    'Pragma': 'no-cache',
    'Referer': 'http://www.sse.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'jsonCallBack': 'jsonpCallback30530284',
    'isPagination': 'true',
    'pageHelp.pageSize': '25',
    'pageHelp.cacheSize': '1',
    'START_DATE': '2023-02-14',
    'END_DATE': '2023-05-14',
    'SECURITY_CODE': '',
    'TITLE': '',
    'BULLETIN_TYPE': '',
    'stockType': '',
    'pageHelp.pageNo': '5',
    'pageHelp.beginPage': '1',#翻页
    'pageHelp.endPage': '5',
    '_': '1684058165995',
}
response = requests.get(
    'http://query.sse.com.cn/security/stock/queryCompanyBulletinNew.do',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
).text
data=re.findall('jsonpCallback30530284\((.*?)\)',response)[0]
# print(data)
#json反序列化: 将json字符串转换成对象
json_obj = json.loads(data)
# print(json_obj)
sa=json_obj['pageHelp']['data']
print(sa)
for list in sa:
    list_TITLE=list[0]['TITLE']#公告标题
    # print(list_TITLE)
    list_BULLETIN_TYPE_DESC=list[0]['BULLETIN_TYPE_DESC']#公告分类
    list_SECURITY_NAME=list[0]['SECURITY_NAME']#证券简称
    list_SSEDATE=list[0]['SSEDATE']#公告时间
    list_SECURITY_CODE=list[0]['SECURITY_CODE']#证券代码
    ju=list[0]['URL']
    list_url='http://static.sse.com.cn/'+ju
    print(list_TITLE,
          list_BULLETIN_TYPE_DESC,
          list_SECURITY_NAME,
          list_SSEDATE,
          list_SECURITY_CODE,
          list_url)
