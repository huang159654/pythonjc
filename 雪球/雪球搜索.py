import re

import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'device_id=2fedb527c524d02cba27f698240bc43c; acw_tc=276077b216859577978984930e0721afb58f34171af50cb795766d6467a3e2; xq_a_token=92653cab19163fc842ad5747ac2c2cdee44c935e; xqat=92653cab19163fc842ad5747ac2c2cdee44c935e; xq_r_token=0f90d6ef86e3c742498591af7860096fe2e3fc86; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY4NzczOTYwMiwiY3RtIjoxNjg1OTU3NzcyNDg3LCJjaWQiOiJkOWQwbjRBWnVwIn0.ilJbR-LZZEQQ30A_TEqEO875Z9kb_e_TEozGndAoEMvaMar1MMogS_Y2LRzcAjKFe-Z_Zh_4-BCoT26icuduz_nqyh7a74Es41MG-9TVQ1GE-d29sVfSpL8yphYJAPkL2jhN0vG5JnlgR-7IJ3tv4YlpMWPz_2zcsWo2C_BiL8NicF-_ucw3Jtr4wRmT6-SaQWHRTgdeLoBoe0CI5p9EwOEMbYugHQFDUSunXk2VKrdb1TDsuAVAyY2sa1r0MJzrwb9c8rocIzboxB7QzzGhuQKp4AhBEIb-nhYrXCiV9eRoEsOlgaltvDLlnXlSpza1svNBdISjiie-EDSmtyeGiQ; u=951685957797904; Hm_lvt_1db88642e346389874251b5a1eded6e3=1685898776,1685957799; s=b112pb6rzd; __utma=1.242745405.1685957871.1685957871.1685957871.1; __utmc=1; __utmz=1.1685957871.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.8.10.1685957871; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1685959011',
    'Pragma': 'no-cache',
    'Referer': 'https://xueqiu.com/hq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'code': 'Aapl',
    'size': '5',
    '_': '1685959027722',
}

response = requests.get('https://xueqiu.com/query/v1/search/stock.json', params=params,headers=headers).json()
# print(response)
stocks = response['stocks'][0]['code']
list_url='https://xueqiu.com/S/'+stocks
response_1=requests.get(url=list_url,headers=headers).text
# print(response_1)
capitalization=re.findall('总市值：&lt;span&gt;(.*?)&lt;',response_1)[1]#总市值
statement=re.findall('rel="next">分红派息</a></li><li><a href="(.*?)"',response_1)[0]#利润表
# statement_url = 'https://xueqiu.com/snowman' + statement
# response_2=requests.get(url=statement_url,ALL_headers=ALL_headers).text
# print(response_2)
all_url=f'https://stock.xueqiu.com/v5/stock/finance/us/income.json?symbol={stocks}&type=all&is_detail=true&count=5&timestamp='#全部
response_all=requests.get(url=all_url,headers=headers).json()
da=response_all['data']['list'][0]['revenue'][0]
print(da)


# url_report=f'https://stock.xueqiu.com/v5/stock/finance/us/income.json?symbol={stocks}&type=Q4&is_detail=true&count=5&timestamp=',#年报
# response_2=requests.get(url=url_report,ALL_headers=ALL_headers).json()
# print()



