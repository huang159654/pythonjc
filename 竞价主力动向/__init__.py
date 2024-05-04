import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://www.wuylh.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.wuylh.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://wuyang.obs.cn-east-2.myhuaweicloud.com/json_data/jhzldx_20230505.json', headers=headers).json()
list_data=response['strategy_ott']
for list in list_data:
    list_name=list['name']#股票名称
    list_code = list['code']  # 股票
    list_pct_25=list['pct_25']#开盘涨幅
    list_close = list['close']  # 实时涨幅
    list_amt_25 = list['amt_25']  # 集合金额
    list_ltsz = list['ltsz']  # 流通市值

