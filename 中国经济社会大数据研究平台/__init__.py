import requests

cookies = {
    'SID': '009102',
    'Ecp_ClientId': '"1230418003300044967"',
    'Ecp_IpLoginFail': '230418120.228.237.71',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'SID=009102; Ecp_ClientId="1230418003300044967"; Ecp_IpLoginFail=230418120.228.237.71',
    'Origin': 'https://data.cnki.net',
    'Pragma': 'no-cache',
    'Referer': 'https://data.cnki.net/valueSearch/index?ky=GDP',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'kd': 'GDP',
    'area': '',
    'dataType': 'year',
    'endYear': 0,
    'beginYear': 0,
    'searchModeOne': 0,
    'sort': 0,
    'groupSearchCon': '',
    'groupType': '',
    'currentPage': 2,
    'pageSize': 20,
    'albumCode': '',
    'type': '',
}

response = requests.post(
    'https://data.cnki.net/api/csyd/ValueSearch/GetOneBoxSearch',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
print(response)