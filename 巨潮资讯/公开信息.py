import requests

cookies = {
    'JSESSIONID': 'C5F5D180D9261F781A493215492656F6',
    '_sp_ses.2141': '*',
    'routeId': '.uc2',
    '_sp_id.2141': 'd3c939ca-d4e8-4843-a86e-88e711e1d020.1681583026.1.1681583352.1681583026.fae8589a-9768-4e47-8379-eba1f3724369',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'JSESSIONID=C5F5D180D9261F781A493215492656F6; _sp_ses.2141=*; routeId=.uc2; _sp_id.2141=d3c939ca-d4e8-4843-a86e-88e711e1d020.1681583026.1.1681583352.1681583026.fae8589a-9768-4e47-8379-eba1f3724369',
    'Origin': 'http://www.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.cninfo.com.cn/new/commonUrl?url=data/public-information',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'sdate': '',
    'edate': '',
    'platecode': '',
    'orderby': '',
    'page': '3',
    'rows': '30',
}

response = requests.post(
    'http://www.cninfo.com.cn/data/statis/getMarketStatisticsData',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
).json()
print(response)