import requests

cookies = {
    'SECKEY_ABVK': 'K8TZ1iwX7OpAKi3BD0Dsa4FeOOHUEGWp99y8xgbJp7I%3D',
    'BMAP_SECKEY': 'DcjyOY2MSdNeDyzCTr36QwSRV4kSwH-qkVLznLSVJBydV1eUfpnDl9NoFKK3VT7aBkFVNrPIr3hFiGcnhrJPwedAVYN6_mGjqxTCB3ZKr9KB5tae3rQPsX69wjTB-urGSHae59AlikknlRO0vLHZY-WWHVBxvArTdwA6Q10VJOWp8whFc3yMqIWYBJCq91PC',
    '__trackId': '4195583775013125',
    'sbxf': '01b3eb371576396691c038db341c3b5e72c',
    'Hm_lvt_5a727f1b4acc5725516637e03b07d3d2': '1687020793',
    'local_flag_guide_shown': '1',
    '__city': 'nanjing',
    '__s': 'lgc9t0n5jrbt3997sr1vt4tpt6',
    'c0fc276cce08ba22dc': 'c858227c49e99b93f0e8cf9226fb4d6d',
    'c1fc276cce08ba22dc': '01b3eb371576396691c038db341c3b5e72c',
    'bxf': '01b3eb371576396691c038db341c3b5e72c',
    'Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2': '1687182530',
    '__sense_session_pv': '5',
}

headers = {
    'authority': 'nanjing.baixing.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'SECKEY_ABVK=K8TZ1iwX7OpAKi3BD0Dsa4FeOOHUEGWp99y8xgbJp7I%3D; BMAP_SECKEY=DcjyOY2MSdNeDyzCTr36QwSRV4kSwH-qkVLznLSVJBydV1eUfpnDl9NoFKK3VT7aBkFVNrPIr3hFiGcnhrJPwedAVYN6_mGjqxTCB3ZKr9KB5tae3rQPsX69wjTB-urGSHae59AlikknlRO0vLHZY-WWHVBxvArTdwA6Q10VJOWp8whFc3yMqIWYBJCq91PC; __trackId=4195583775013125; sbxf=01b3eb371576396691c038db341c3b5e72c; Hm_lvt_5a727f1b4acc5725516637e03b07d3d2=1687020793; local_flag_guide_shown=1; __city=nanjing; __s=lgc9t0n5jrbt3997sr1vt4tpt6; c0fc276cce08ba22dc=c858227c49e99b93f0e8cf9226fb4d6d; c1fc276cce08ba22dc=01b3eb371576396691c038db341c3b5e72c; bxf=01b3eb371576396691c038db341c3b5e72c; Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2=1687182530; __sense_session_pv=5',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'from': 'regular',
}

response = requests.get('https://nanjing.baixing.com/wenmi/a2619352097.html', params=params, cookies=cookies, headers=headers)
response.encoding=response.apparent_encoding