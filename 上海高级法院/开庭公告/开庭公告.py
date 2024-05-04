import json
import re
import time
import random
import requests
import csv
f = open('上海市高级法院开庭公告.csv', mode='a', encoding='utf_8_sig', newline='\n')
csv_writer = csv.DictWriter(f, fieldnames=[
    '法庭',
    '法庭_1',
    '开庭日期',
    '案号',
    '案由',
    '承办部门',
    '审判长/主审人',
    '原告/上诉人',
    '被告/被上诉人',
    '开庭类型',
])
cookies = {
    'JSESSIONID': 'E912938BC2F62992FC932269633735D3-n1',
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'JSESSIONID=E912938BC2F62992FC932269633735D3-n1',
    'Origin': 'https://www.hshfy.sh.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.hshfy.sh.cn/shfy/web/ktgg_search.jsp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
for pagesnum in range(1,3075):
    data = {
        'yzm': 'c5dx',
        'ft': '',
        'ktrqks': '2023-06-19',
        'ktrqjs': '2023-07-19',
        'spc': '',
        'yg': '',
        'bg': '',
        'ah': '',
        'pagesnum': pagesnum,
        'ktlx': '',
    }
    print(f'正在打印第{pagesnum}页')
    time.sleep(random.randint(3, 20))
    response = requests.post('https://www.hshfy.sh.cn/shfy/web/ktgg_search_content.jsp', cookies=cookies, headers=headers, data=data).text
    court_da=re.findall("\<TD class\=10dpi width\=48 align\=\'center\'\>\<FONT color\=\#000000\>(.*?)\<span class\=\"word7\"\>\<font color\=\"\#C00307\"\>\*\<\/font\>\<\/span\>\&nbsp\;\<\/FONT\>\<\/TD\>",response)#法庭
    court=re.findall("\<TD class\=10dpi width\=80 align\=\'center\'\>\<FONT color\=\#000000\>(.*?)\&nbsp\;\<\/FONT\>\<\/TD\>",response)#法庭
    Court_date=re.findall('\<TD class\=10dpi width\=75 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>',response)#开庭日期
    Case_number=re.findall("\<TD class\=10dpi width\=120 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>",response)#案号
    Case_brief=re.findall("\<TD class\=10dpi width\=90 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>",response)#案由
    Undertaking_department=re.findall("\<TD class\=10dpi width\=60 align\=\'center\'\>\<div align\=\"center\"\>(.*?)\&nbsp\;\<\/div\>\<\/TD\>",response)#承办部门
    Presiding_Judge=re.findall("\<TD class\=10dpi width\=75 align\=\'center\'\>\<div align\=\"center\"\>(.*?)\&nbsp\;\<\/div\>\<\/TD\>",response)#审判长/主审人
    Plaintiff_Appellant=re.findall("\<TD class\=10dpi width\=130 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>",response)#原告/上诉人
    Defendant_Appellant=re.findall("\<TD class\=10dpi width\=140 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>",response)#被告/被上诉人
    Type_hearing=re.findall("\<TD class\=10dpi width\=140 align\=\'center\'\>(.*?)\&nbsp\;\<\/TD\>",response)#开庭类型
    for d,data,sa,s,da,fs,xz,kd,si,dx, in zip(court_da,court,Court_date,Case_number,Case_brief,Undertaking_department,Presiding_Judge,Plaintiff_Appellant,Defendant_Appellant,Type_hearing):
        dit = {
            '法庭':d,
            '法庭_1':data,
            '开庭日期':sa,
            '案号':s,
            '案由':da,
            '承办部门':fs,
            '审判长/主审人':xz,
            '原告/上诉人':kd,
            '被告/被上诉人':si,
            '开庭类型':dx,
        }
        print('下载完毕!',d,data,sa,s,da,fs,xz,kd,si,dx,)
        csv_writer.writerow(dit)
