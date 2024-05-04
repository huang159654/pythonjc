import pprint

import requests

headers = {
    'authority': 'api.kgd.ltd',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://web.kgd.ltd',
    'pragma': 'no-cache',
    'referer': 'https://web.kgd.ltd/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

json_data = {
    'enterprise_id': '10597',
    'token': 'd824b2d0eb01ca6d59078cade0718207',
    'type': 1,
    'pageNo': 2,
    'pageSize': 30,
    'timestamp': 1686914443,
    'sign': '78b8f4a88d76503fda61296a39a62d54',
    'channel': 1,
}

response = requests.post('https://api.kgd.ltd/api/produce_bill/web_list', headers=headers, json=json_data).json()
list_data=response.get('data')
print(response)