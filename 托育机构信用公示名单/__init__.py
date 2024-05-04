import csv
import datetime

import requests

f = open('托育机构信用公示名单.csv', mode='a', encoding='utf_8_sig', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '下载时间',
    '机构注册登记名称',
    '所属区域',
    '机构住所',
    '机构性质',
    '备案通过时间',
    '统一社会信用代码'
])
csv_writer.writeheader()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://tuoyu.cpdrc.org.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
i = datetime.datetime.now()
for pageNum in range(1, 2867):
    print(f'正在下载第{pageNum}页')
    params = {
        'pageSize': '10',
        'pageNum': pageNum,
        'key': '',
    }

    response = requests.get('https://tuoyu.cpdrc.org.cn/bapfopm/pub/search/action/queryInfo', params=params,
                            headers=headers).json()
    list = response.get('responseData').get('dataList')
    for list_s in list:
        institution_name = list_s.get('institution_name')  # 机构注册登记名称
        zoning_name = list_s.get('zoning_name')  # 所属区域
        address = list_s.get('address')  # 机构住所
        institution_type = list_s.get('institution_type')  # 机构性质
        finished_time = list_s.get('finished_time')  # 备案通过时间
        credit_code = list_s.get('credit_code')  # 统一社会信用代码
        dit = {
            '下载时间':i,
            '机构注册登记名称':institution_name,
            '所属区域': zoning_name,
            '机构住所': address,
            '机构性质': institution_type,
            '备案通过时间': finished_time,
            '统一社会信用代码': credit_code,
 }
        csv_writer.writerow(dit)
        print('下载完毕!', i, institution_name, zoning_name, address, institution_type, finished_time, credit_code)
