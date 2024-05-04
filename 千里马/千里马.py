import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://www.qianlima.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.qianlima.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'areas': '',
    'jzjd': '',
    'xmType': '',
    'ownerType': '',
    'decorationStatus': '',
    'keywords': '',
    'numPerPage': '30',
    'currentPage': '2',
}

response = requests.post('https://search.qianlima.com/api/v1/willBuild/search', params=params, headers=headers).json()
print(response)