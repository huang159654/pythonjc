
import requests

cookies = {
    'JSESSIONID': 'B39B4F69F7367EF3512CB51A262D28E9',
    'BIGipServerPool_BIWADP-APP_8080': '!uMpBmq7wjVX+YFIDqSlfD6KqyuVpAmoBFcokneAqKWmpsXTSH/B6cA7MD4H0t/m+32OwoELBs+0lyp0=',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/cnap-message',
    # 'Cookie': 'JSESSIONID=B39B4F69F7367EF3512CB51A262D28E9; BIGipServerPool_BIWADP-APP_8080=!uMpBmq7wjVX+YFIDqSlfD6KqyuVpAmoBFcokneAqKWmpsXTSH/B6cA7MD4H0t/m+32OwoELBs+0lyp0=',
    'Origin': 'https://www.chinabond.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.chinabond.com.cn/greenbond/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',}

for page in range(1, 28):
    data = '{"header":{"sendSysname":"lvzhai","msgType":"gbbsw.vue",' \
           '"msgId":"lvzhai1627524838671271b69c4368470ea685650d08cc4dd31","sendTime":"2023/5/4 14:40:13","exts":{}},' \
           '"body":{"version":"1.1","trnsType":"gbbsw.vue",' \
           '"trnsId":"lvzhai1627524838671271b69c4368470ea685650d08cc4dd31","exts":{"bondCode":"","bondNameAbbr":"",' \
           '"province":"","greenDigree":"","bondType":"","ebero":"","page":%d,"pageSize":10,"startTime":"",' \
           '"endTime":""}}}' % page

    response = requests.post(
            'https://www.chinabond.com.cn/gbebsm/searchBondPublishedList',
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()
    list_data=response['body']['exts']['pageInfo']['list']
    for list_da in list_data:
        bondName_Abbr=list_da['bondNameAbbr']#债券简称
        bond_Code = list_da['bondCode']#债券代码
        issuerClient_Name = list_da['issuerClientName']  # 发行人
        bond_Type = list_da['bondType']  # 债券类型
        ebero = list_da['ebero']  # 托管机构
        prov_ince = list_da['province']  # 省份
        issueIndustry_Code1 = list_da['issueIndustryCode1']  # 发行人所属行业
        isin = list_da['isin']  # ISIN代码
        issue_Date = list_da['issueDate']  # 发行时间
        dueDate = list_da['dueDate']  # 到期日
        thirdOrgani_zation = list_da['thirdOrganization']  # 第三方认证机构



        print(bondName_Abbr,
              bond_Code,
              issuerClient_Name,
              bond_Type,
              ebero,
              prov_ince,
              issueIndustry_Code1,
              isin,
              issue_Date,
              dueDate,
              thirdOrgani_zation)
    break
