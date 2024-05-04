import requests

cookies = {
    'buvid3': '1569D395-9D78-2097-3A05-068919EA3E3138547infoc',
    'b_nut': '1680957938',
    'CURRENT_FNVAL': '4048',
    '_uuid': '2710BDD9A-E32F-1CEE-51046-5E9103DDE9A7B39198infoc',
    'buvid_fp': 'c9a3c40d61e4d906ba4f07b603104aca',
    'CURRENT_PID': '4477a730-d60b-11ed-927c-192fc085b4ab',
    'rpdid': "|(k|k)kY))~u0J'uY)|ml~mR|",
    'i-wanna-go-back': '-1',
    'header_theme_version': 'CLOSE',
    'home_feed_column': '4',
    'nostalgia_conf': '-1',
    'buvid4': '32D3DCCD-67F0-CD20-4EA5-BD74CFFF7FD139701-023040820-QpV8FfJYhXQVlLE2OsB%2FbA%3D%3D',
    'browser_resolution': '1280-587',
    'PVID': '1',
    'DedeUserID': '3493299218287290',
    'DedeUserID__ckMd5': '554097768e9c6901',
    'b_ut': '5',
    'FEED_LIVE_VERSION': 'V_SIDE_CARD_REFRESH',
    'CURRENT_QUALITY': '64',
    'bp_video_offset_3493299218287290': 'undefined',
    'b_lsid': 'E995F368_1884825EB51',
    'bsource': 'search_baidu',
    'SESSDATA': 'ea57b7a2%2C1700389629%2C2b8ff%2A52',
    'bili_jct': 'c36eb96bd71107e8199bb8249a7ab93d',
    'innersign': '1',
    'sid': 'fi7mdg7v',
}

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': "buvid3=1569D395-9D78-2097-3A05-068919EA3E3138547infoc; b_nut=1680957938; CURRENT_FNVAL=4048; _uuid=2710BDD9A-E32F-1CEE-51046-5E9103DDE9A7B39198infoc; buvid_fp=c9a3c40d61e4d906ba4f07b603104aca; CURRENT_PID=4477a730-d60b-11ed-927c-192fc085b4ab; rpdid=|(k|k)kY))~u0J'uY)|ml~mR|; i-wanna-go-back=-1; header_theme_version=CLOSE; home_feed_column=4; nostalgia_conf=-1; buvid4=32D3DCCD-67F0-CD20-4EA5-BD74CFFF7FD139701-023040820-QpV8FfJYhXQVlLE2OsB%2FbA%3D%3D; browser_resolution=1280-587; PVID=1; DedeUserID=3493299218287290; DedeUserID__ckMd5=554097768e9c6901; b_ut=5; FEED_LIVE_VERSION=V_SIDE_CARD_REFRESH; CURRENT_QUALITY=64; bp_video_offset_3493299218287290=undefined; b_lsid=E995F368_1884825EB51; bsource=search_baidu; SESSDATA=ea57b7a2%2C1700389629%2C2b8ff%2A52; bili_jct=c36eb96bd71107e8199bb8249a7ab93d; innersign=1; sid=fi7mdg7v",
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://www.bilibili.com/video/BV15P411d7kS/?spm_id_from=333.337.search-card.all.click&vd_source=97dd4bf7757e3c504baea19b6888ae43',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://api.bilibili.com/x/v2/reply/main?csrf=c36eb96bd71107e8199bb8249a7ab93d&mode=3&oid=313729017&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&type=1',
    cookies=cookies,
    headers=headers,
).json()
data_dict=response.get('data').get('replies')
for div in data_dict:
    div_uname = div.get('member').get('uname')#用户名
    div_message = div.get('content').get('message')  # 评论文本
    print(div_uname,div_message)