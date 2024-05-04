import re

import requests

url = 'https://finance.sina.com.cn/topnews/20080216.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding #中文乱码转换
html_data=response.text
data_list=re.findall("<span style='padding-left:6px'><a href=(.*?) target=_blank>(.*?)</a></span></td>",html_data)
for i in data_list:
    da=i[0]
    print(da)
