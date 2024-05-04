import json
import re

import requests

cookies = {
    '__jdu': '1686813996937146638967',
    'areaId': '16',
    'shshshfpb': 'aHsQuf_pnhNYVhQy1E_dtJw',
    'shshshfpa': '735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713',
    'shshshfpx': '735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713',
    'ipLoc-djd': '16-1332-1334-43086',
    'unpl': 'JF8EAMdnNSttWk4EUBsETEIQHg1UW1pcTh9UbWIDUw1RSAcMGFYbGxJ7XlVdXxRKEB9vYRRUWFNJUQ4bBSsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwbF0JdVlZVD0MVBW9iAlNfUUNTAysDKxUge21XVlUIQicCX2Y1FgkEQ1MDEgEaXxBMVFNXXQpDHwRnZQNUWF9MVgwTBR0iEXte',
    '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_34ad17fa1da146e49f3476a82b82e183|1686983655982',
    '3AB9D23F7A4B3C9B': 'M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQA',
    'jsavif': '1',
    '3AB9D23F7A4B3CSS': 'jdd03M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQAAAAAMIZZUAQTYAAAAADYMOG6AM6ZOVYMX',
    '_gia_d': '1',
    '__jda': '122270672.1686813996937146638967.1686813996.1686983656.1687089930.5',
    '__jdb': '122270672.2.1686813996937146638967|5.1687089930',
    '__jdc': '122270672',
}

headers = {
    'authority': 'api.m.jd.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__jdu=1686813996937146638967; areaId=16; shshshfpb=aHsQuf_pnhNYVhQy1E_dtJw; shshshfpa=735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713; shshshfpx=735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713; ipLoc-djd=16-1332-1334-43086; unpl=JF8EAMdnNSttWk4EUBsETEIQHg1UW1pcTh9UbWIDUw1RSAcMGFYbGxJ7XlVdXxRKEB9vYRRUWFNJUQ4bBSsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwbF0JdVlZVD0MVBW9iAlNfUUNTAysDKxUge21XVlUIQicCX2Y1FgkEQ1MDEgEaXxBMVFNXXQpDHwRnZQNUWF9MVgwTBR0iEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_34ad17fa1da146e49f3476a82b82e183|1686983655982; 3AB9D23F7A4B3C9B=M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQA; jsavif=1; 3AB9D23F7A4B3CSS=jdd03M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQAAAAAMIZZUAQTYAAAAADYMOG6AM6ZOVYMX; _gia_d=1; __jda=122270672.1686813996937146638967.1686813996.1686983656.1687089930.5; __jdb=122270672.2.1686813996937146638967|5.1687089930; __jdc=122270672',
    'origin': 'https://search.jd.com',
    'pragma': 'no-cache',
    'referer': 'https://search.jd.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-referer-page': 'https://search.jd.com/Search',
    'x-rp-client': 'h5_1.0.0',
}

url='https://api.m.jd.com/api?functionId=pc_search_adv_Search&appid=search-pc-java&client=pc&clientVersion=1.0.0&uuid=122270672.1686813996937146638967.1686813996.1686983656.1687089930.5&loginType=3&t=1687090103454&body={%22area%22:%2216%22,%22enc%22:%22utf-8%22,%22keyword%22:%22%E7%AC%94%E8%AE%B0%E6%9C%AC%22,%22adType%22:7,%22page%22:%221%22,%22ad_ids%22:%22291:60%22,%22xtest%22:%22new_search%22}&x-api-eid-token=jdd03M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQAAAAAMIZZUAQTYAAAAADYMOG6AM6ZOVYMX'

response = requests.get(
    url=url,
    cookies=cookies,
    headers=headers,
).json()
list_data=response.get('291')
version=[]
color=[]
for list in list_data:
    div_ad=list.get('ad_title')#名字
    div_ad_title=div_ad.replace('<font class="skcolor_ljg">','').replace('</font>','')#替换名字没有的
    div_pc_price=list.get('pc_price')+'元' #价格
    div_fuzzy_comment_num=list.get('fuzzy_comment_num')#评论
    div_shop_name=list.get('shop_link').get('shop_name') #店名
    div_shop_id=list.get('sku_id')#详情页id
    # print(div_shop_id)
    id_url=f'https://item.jd.com/{div_shop_id}.html'
    #商品详情页
    response_1=requests.get(url=id_url,headers=headers,cookies=cookies).text
    # print(response_1)
    df=re.findall('"(.*?)","skuId":.*?,"(.*?)"}',response_1)
    for list_d in df:
        # print()
        sa=list_d[0].replace('"','')
        so = list_d[1].replace('"', '')
        version.append(sa)#版本
        color.append(so)#颜色
    print(div_ad,div_ad_title,div_pc_price,div_fuzzy_comment_num,div_shop_name,version,color)
    #商品评论
    params = {
        'appid': 'item-v3',
        'functionId': 'pc_club_productPageComments',
        'client': 'pc',
        'clientVersion': '1.0.0',
        't': '1685778856241',
        'loginType': '3',
        'uuid': '122270672.1682280713762127348183.1682280714.1684864173.1685776424.8',
        'productId':div_shop_id ,
        'score': '0',
        'sortType': '5',
        'page': '1',
        'pageSize': '10',
        'isShadowSku': '0',
        'rid': '0',
        'fold': '1',
        'bbtf': '',
        'shield': '',
    }
    response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers).json()
    list_data = response['comments']
    for i in list_data:
        try:
            list_content = i['content']  # 评论文本
            list_creationTime = i['creationTime']  # 评论时间
            list_location = i['location']  # IP地址
            list_referenceName = i['referenceName']  # 评论电脑名字
            print(list_content,
                  list_creationTime,
                  list_location,
                  list_referenceName)
        except Exception as e:
            e
    break