import csv
import re
import requests
import pandas
neme=input('请输入保存的文件名字:')
cookies = {
    'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690536714',
    'Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208': '1690555297',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1690536714; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1690555297',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
i=1
while True:
    if i < 21:
        print(f'正在下载{i}页')
        response = requests.get(f'https://product.11467.com/jiaolun/pn{i}/', cookies=cookies, headers=headers).text
        name=re.findall('\<div class\=\"btn\-mobile\"\>.*?\<\/div\>\<\/dd\>\<dd\>\<a href\=\".*?"\>(.*?)<\/a\>',response)
        da=re.findall('\<div class\=\"btn\-mobile\"\>(.*?)\<\/div\>',response)#电话号码
        # print(da)
        i += 1
        df = pandas.DataFrame({'电话号码': da,
                               '公司名称': name,
                               })
        df.to_csv(f'{neme}.csv', mode='a', index=False, encoding='utf_8_sig')
        print(da,name)
    else:
        break

