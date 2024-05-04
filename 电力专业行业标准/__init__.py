import re
import requests
from rich.console import Console
from rich import inspect
console = Console()

cookies = {
    'Hm_lvt_ac3f24c58d6856a28f4da49c5ade057f': '1687099471',
    'ASP.NET_SessionId': 'ube0rrhsygsxr4g2qgz1hziw',
    'Hm_lpvt_ac3f24c58d6856a28f4da49c5ade057f': '1687099476',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_ac3f24c58d6856a28f4da49c5ade057f=1687099471; ASP.NET_SessionId=ube0rrhsygsxr4g2qgz1hziw; Hm_lpvt_ac3f24c58d6856a28f4da49c5ade057f=1687099476',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

response = requests.get('http://www.jianbiaoku.com/webarbs/list/187/1.shtml', cookies=cookies, headers=headers, verify=False)
response.encoding=response.apparent_encoding
sa=response.text
dsu=re.findall('<span class="book_date">(.*?)</span>',sa)#更新日期
for ids in dsu:
    update_date=ids.replace('更新日期','')
    # print(update_date)
list_time =re.findall('<span class="book_version" title="(.*?)">.*?</span>',sa)#编号
for da in list_time:
    numbering=da#编号
    # print(numbering)
fd=re.findall('<a href=".*?" title="(.*?)" .*?</a>',sa)#书名
for i in fd:
    titie=i
    # info=[titie,update_date,numbering]
    console.rule('分割线')
    console.log(titie,update_date,numbering)

    # inspect(info)
