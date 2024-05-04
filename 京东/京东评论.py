import requests

cookies = {
    'shshshfp': 'd26a0160c1afe296805bcf71f1462365',
    'shshshfpa': '735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713',
    'shshshfpx': '735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713',
    '__jdu': '1682280713762127348183',
    'jcap_dvzw_fp': 'zpnHD6TuJmIB-EWaOY59Ev6tMrbsPZONr49im9o7JMUM6mcTQW9ljyePrXrm3XDGHrS9PPqKKGfOg8lnO8uhIw==',
    'shshshfpb': 'aHsQuf_pnhNYVhQy1E_dtJw',
    'areaId': '17',
    'ipLoc-djd': '17-1432-1435-0',
    'unpl': 'JF8EAMdnNSttCkJTBUwDT0AUG1hSW1ldTx9QaGEEXVUMG1VQGFAaFEV7XlVdXxRKEB9uZRRUWVNLVg4eACsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwbE0hUVVhdCk0QAG9kA1ZYUUtdBysDKxUge21UXlkLTicCX2Y1FgkEQlIMHQQcXxBMVFddVAlNFwFpYAZUXl5JUQwbCxkiEXte',
    '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_c861f0ec5a4745d59b67089ea0d2c07d|1685776423733',
    'jsavif': '1',
    '__jda': '122270672.1682280713762127348183.1682280714.1684864173.1685776424.8',
    '__jdc': '122270672',
    '3AB9D23F7A4B3C9B': 'M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQA',
    'token': '744488e3c63b30606f47973d4b6b92b4,2,936543',
    '__tk': '1c17d20756a1a93cf21f28191638a5cd,2,936543',
    'shshshsID': 'b62bcc3d1c6f2f089eab85a3e9740971_3_1685778776648',
    '3AB9D23F7A4B3CSS': 'jdd03M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQAAAAAMIQA7MLSQAAAAADZ2ARFF7HFZLDYX',
    '_gia_d': '1',
    '__jdb': '122270672.4.1682280713762127348183|8.1685776424',
}

headers = {
    'authority': 'api.m.jd.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=gbk',
    # 'cookie': 'shshshfp=d26a0160c1afe296805bcf71f1462365; shshshfpa=735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713; shshshfpx=735b9909-42a0-f6d9-6359-af4b883fdf54-1682280713; __jdu=1682280713762127348183; jcap_dvzw_fp=zpnHD6TuJmIB-EWaOY59Ev6tMrbsPZONr49im9o7JMUM6mcTQW9ljyePrXrm3XDGHrS9PPqKKGfOg8lnO8uhIw==; shshshfpb=aHsQuf_pnhNYVhQy1E_dtJw; areaId=17; ipLoc-djd=17-1432-1435-0; unpl=JF8EAMdnNSttCkJTBUwDT0AUG1hSW1ldTx9QaGEEXVUMG1VQGFAaFEV7XlVdXxRKEB9uZRRUWVNLVg4eACsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwbE0hUVVhdCk0QAG9kA1ZYUUtdBysDKxUge21UXlkLTicCX2Y1FgkEQlIMHQQcXxBMVFddVAlNFwFpYAZUXl5JUQwbCxkiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_c861f0ec5a4745d59b67089ea0d2c07d|1685776423733; jsavif=1; __jda=122270672.1682280713762127348183.1682280714.1684864173.1685776424.8; __jdc=122270672; 3AB9D23F7A4B3C9B=M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQA; token=744488e3c63b30606f47973d4b6b92b4,2,936543; __tk=1c17d20756a1a93cf21f28191638a5cd,2,936543; shshshsID=b62bcc3d1c6f2f089eab85a3e9740971_3_1685778776648; 3AB9D23F7A4B3CSS=jdd03M6SZMBQY7BMIGJA4TL2VOIR7GIL7LLMLOSA4KPO2WNEAYNCC67JLKUGL6PYZGV5F4NEIMUGA4G5VY65L2ZFKB6ABQAAAAAMIQA7MLSQAAAAADZ2ARFF7HFZLDYX; _gia_d=1; __jdb=122270672.4.1682280713762127348183|8.1685776424',
    'origin': 'https://item.jd.com',
    'pragma': 'no-cache',
    'referer': 'https://item.jd.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-referer-page': 'https://item.jd.com/100042885947.html',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    'appid': 'item-v3',
    'functionId': 'pc_club_productPageComments',
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': '1685778856241',
    'loginType': '3',
    'uuid': '122270672.1682280713762127348183.1682280714.1684864173.1685776424.8',
    'productId': '100042885947',
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
list_data=response['comments']
for i in list_data:
    try:
        list_content=i['content']#评论文本
        list_creationTime = i['creationTime']  # 评论时间
        list_location = i['location']  # IP地址
        list_referenceName = i['referenceName']  # 评论电脑名字
        print(list_content,
              list_creationTime,
              list_location,
              list_referenceName)
    except Exception as e:
        e