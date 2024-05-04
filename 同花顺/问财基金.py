import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'other_uid=Ths_iwencai_Xuangu_7gd15gfhl7u9q3ppwx2o3rsl11gobfls; ta_random_userid=4f9udt8qhb; cid=ca8e98d7ed75e178118272473ddc69c01686995253; v=AxDv59RbQOVZqxwH4rlyB82c4VVn2f9pFqxI4Qrh3Ec-iL5LsunEs2bNGKtZ',
    'Origin': 'https://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=%E8%85%BE%E8%AE%AF&querytype=fund&issugs&sign=1687181386493',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    #'hexin-v': 'AxDv59RbQOVZqxwH4rlyB82c4VVn2f9pFqxI4Qrh3Ec-iL5LsunEs2bNGKtZ',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
data = {
    'query': '腾讯',
    'condition': '[{"indexName":"基金@重仓股股票名称","indexProperties":["nodate 1","概念id 302010","起始交易日期 20230331","截止交易日期 20230331","包含腾讯控股"],"source":"new_parser","type":"index","indexPropertiesMap":{"概念id":"302010","起始交易日期":"20230331","截止交易日期":"20230331","包含":"腾讯控股","nodate":"1"},"reportType":"QUARTER","dateType":"报告期","chunkedResult":"腾讯","valueType":"_重仓股股票名称","domain":"abs_基金领域","uiText":"重仓股股票名称是腾讯控股","sonSize":0,"queryText":"重仓股股票名称是腾讯控股","relatedSize":0,"tag":"基金@重仓股股票名称"}]',
    'urp_sort_index': '',
    'source': 'Ths_iwencai_Xuangu',
    'perpage': '50',
    'page': '2',
    'urp_sort_way': '',
    'codelist': '',
    'page_id': '',
    'logid': '02cd07b33b44851c319c27b899bd0063',
    'ret': 'json_all',
    'sessionid': '02cd07b33b44851c319c27b899bd0063',
    'iwc_token': '0ac9665916871813884308650',
    'user_id': 'Ths_iwencai_Xuangu_7gd15gfhl7u9q3ppwx2o3rsl11gobfls',
    'uuids[0]': '24088',
    'query_type': 'fund',
    'comp_id': '6757566',
    'business_cat': 'soniu',
    'uuid': '24088',
}

response = requests.post('https://www.iwencai.com/gateway/urp/v7/landing/getDataList',headers=headers, data=data).json()
list=response.get('answer').get('components')[0].get('data').get('datas')
# print(list)
for da in list:
    try:
        stock_symbol=da.get('基金代码')#基金代码
        stock_abbreviation=da.get('基金简称')#基金简称
        current=da.get('基金@最新单位净值')+'元'#基金@最新单位净值元
        price=da.get('基金@最新日收益率')#基金@最新日收益率
        conceptual=da.get('基金@最新净值日期')#基金@最新净值日期
        conceptual_information=da.get('基金@重仓股市值占基金资产净值比[20230331]')#基金@重仓股市值占基金资产净值比[20230331]
        affiliation_concept=da.get('基金@重仓股持股市值[20230331]')#基金@重仓股持股市值[20230331]
        a_value=da.get('基金@重仓股持股数量[20230331]')#基金@重仓股持股数量[20230331]
        belongs=da.get('基金@重仓股持仓变动[20230331]')#基金@重仓股持仓变动[20230331]
        heavy_stocks = da.get('基金@持有重仓股票的基金个数[20230331]')  # 基金@持有重仓股票的基金个数[20230331]
        Stock_name = da.get('基金@重仓股股票名称[20230331]')  # 基金@重仓股股票名称[20230331]
        print(conceptual_information)
        break
    except Exception as e:
        e