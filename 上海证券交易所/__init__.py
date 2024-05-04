import requests

cookies = {
    'ba17301551dcbaf9_gdp_user_key': '',
    'ba17301551dcbaf9_gdp_session_id': '69aa7da9-3e4b-48c9-9322-f3a62f05cac5',
    'gdp_user_id': 'gioenc-24d7837e%2C37e0%2C54d2%2Ccc1a%2C2g384dg01e29',
    'ba17301551dcbaf9_gdp_session_id_69aa7da9-3e4b-48c9-9322-f3a62f05cac5': 'true',
    'VISITED_MENU': '%5B%228349%22%5D',
    'ba17301551dcbaf9_gdp_sequence_ids': '{%22globalKey%22:7%2C%22VISIT%22:2%2C%22PAGE%22:6}',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'ba17301551dcbaf9_gdp_user_key=; ba17301551dcbaf9_gdp_session_id=69aa7da9-3e4b-48c9-9322-f3a62f05cac5; gdp_user_id=gioenc-24d7837e%2C37e0%2C54d2%2Ccc1a%2C2g384dg01e29; ba17301551dcbaf9_gdp_session_id_69aa7da9-3e4b-48c9-9322-f3a62f05cac5=true; VISITED_MENU=%5B%228349%22%5D; ba17301551dcbaf9_gdp_sequence_ids={%22globalKey%22:7%2C%22VISIT%22:2%2C%22PAGE%22:6}',
    'Pragma': 'no-cache',
    'Referer': 'http://www.sse.com.cn/disclosure/listedinfo/announcement/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'v': '0.7364651437571963',
}

response = requests.get(
    'http://www.sse.com.cn/disclosure/listedinfo/announcement/json/stock_bulletin_publish_order.json',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
).json()
json_data = response['publishData']
print(json_data)