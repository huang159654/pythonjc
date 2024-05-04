import pprint

import requests

# cookies = {
#     'other_uid': 'Ths_iwencai_Xuangu_7gd15gfhl7u9q3ppwx2o3rsl11gobfls',
#     'ta_random_userid': '4f9udt8qhb',
#     'cid': 'ca8e98d7ed75e178118272473ddc69c01686995253',
#     'v': 'AyvU1sPiy_8hjBerB7sJxpLFukQQQDzouVADLp2mB03BgUU6JRDPEskkk-Ou',
# }

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'other_uid=Ths_iwencai_Xuangu_7gd15gfhl7u9q3ppwx2o3rsl11gobfls; ta_random_userid=4f9udt8qhb; cid=ca8e98d7ed75e178118272473ddc69c01686995253; v=AyvU1sPiy_8hjBerB7sJxpLFukQQQDzouVADLp2mB03BgUU6JRDPEskkk-Ou',
    'Origin': 'https://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=%E8%85%BE%E8%AE%AF&querytype=stock&issugs&sign=1686997552055',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # 'hexin-v': 'AyvU1sPiy_8hjBerB7sJxpLFukQQQDzouVADLp2mB03BgUU6JRDPEskkk-Ou',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'query': '腾讯',
    'urp_sort_way': 'desc',
    'urp_sort_index': '最新涨跌幅',
    'page': '1',
    'perpage': '100',
    'addheaderindexes': '',
    'condition': '[{"indexName":"所属概念","indexProperties":["概念id 302010","包含腾讯概念"],"source":"new_parser","type":"index","indexPropertiesMap":{"概念id":"302010","包含":"腾讯概念"},"reportType":"null","chunkedResult":"腾讯","valueType":"_所属概念","domain":"abs_股票领域","uiText":"所属概念是腾讯","sonSize":0,"queryText":"所属概念是腾讯","relatedSize":0,"tag":"所属概念"}]',
    'codelist': '',
    'indexnamelimit': '',
    'logid': '30ad9938c3a17effe0e74aa4cac61044',
    'ret': 'json_all',
    'sessionid': '30ad9938c3a17effe0e74aa4cac61044',
    'source': 'Ths_iwencai_Xuangu',
    'date_range[0]': '20230617',
    'iwc_token': '0ac9667016869975526961688',
    'urp_use_sort': '1',
    'user_id': 'Ths_iwencai_Xuangu_7gd15gfhl7u9q3ppwx2o3rsl11gobfls',
    'uuids[0]': '24087',
    'query_type': 'stock',
    'comp_id': '6734520',
    'business_cat': 'soniu',
    'uuid': '24087',
}

response = requests.post('https://www.iwencai.com/gateway/urp/v7/landing/getDataList', headers=headers, data=data).json()
list=response.get('answer').get('components')[0].get('data').get('datas')
for da in list:
    try:
        stock_symbol=da.get('code')#股票代码
        stock_abbreviation=da.get('股票简称')#股票简称
        current=da.get('最新价')+'元'#现价元
        price=da.get('最新涨跌幅')#最新涨跌幅
        conceptual=da.get('概念解析')#概念解析
        conceptual_information=da.get('概念资讯')#概念资讯
        affiliation_concept=da.get('所属概念数量')#所属概念数量
        a_value=da.get('a股市值(不含限售股)[20230616]')#a股市值(不含限售股)[20230616]
        belongs=da.get('所属概念')#所属概念
        print(conceptual_information)
        break
    except Exception as e:
        e