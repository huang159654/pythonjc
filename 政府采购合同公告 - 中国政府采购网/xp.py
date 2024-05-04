import csv

import requests
import parsel
f=open('v_147.csv',mode='a',encoding='utf-8',newline='')
csv_writer=csv.DictWriter(f,fieldnames=[
    '项目名称',
    '发布日期',
    '采购人',
    '供应商',
    '签订时间',
])
csv_writer.writeheader()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONIDGS8=N53pvkvMXAzInw3cqmOGzwymQPZa2wNaN3MiS3PIjGw6cgjRbzAi!1130949133; cookieinsert=20111184; Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1683253876; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1683253876',
    'Pragma': 'no-cache',
    'Referer': 'http://htgs.ccgp.gov.cn/GS8/contractpublish/search?contractSign=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
for i in range(1,56):
    print(f'=============正在下载{i}页=============')
    response = requests.get(f'http://htgs.ccgp.gov.cn/GS8/contractpublish/index_{i}', headers=headers, verify=False).text
    data=parsel.Selector(response)
    list_s=data.xpath('.//div[@class="vT_list_main"]/div/ul/li')
    for div in list_s:
        try:
            div_titie=div.xpath('.//a/text()').get().strip()#项目名称
            div_date = div.xpath('.//span/text()').get().strip()  # 发布日期
            div_Purchaser = div.xpath('.//span/text()')[2].get().strip()  #   采购人
            div_supplier = div.xpath('.//span/text()')[3].get().strip()  #  供应商：
            div_time = div.xpath('.//div/span/text()').get().strip()  # 签订时间：
            print('下载完毕！',div_titie,div_date,div_Purchaser,div_supplier,div_time)
            dit = {
                '项目名称': div_titie,
                '发布日期': div_date,
                '采购人': div_Purchaser,
                '供应商': div_supplier,
                '签订时间': div_time,
            }
            csv_writer.writerow(dit)
        except Exception as e:
            e