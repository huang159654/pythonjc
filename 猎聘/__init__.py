import requests

cookies = {
    'XSRF-TOKEN': 'ysT0K0X3RYidU-KYK3nk5Q',
    '__gc_id': 'c84b29f57afe4d2c895e712725bc36d9',
    '_ga': 'GA1.1.296539765.1686998466',
    '__uuid': '1686998466329.74',
    '__tlog': '1686998466337.60%7C00000000%7C00000000%7C00000000%7C00000000',
    'acw_tc': 'ac11000116869984669203118e00cda4ac00996057bb86efd7b98636608823',
    'Hm_lvt_a2647413544f5a04f00da7eee0d5e200': '1686998467',
    'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200': '1686998583',
    '_ga_54YTJKWN86': 'GS1.1.1686998465.1.1.1686998599.0.0.0',
    '__session_seq': '8',
    '__uv_seq': '8',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8;',
    # 'Cookie': 'XSRF-TOKEN=ysT0K0X3RYidU-KYK3nk5Q; __gc_id=c84b29f57afe4d2c895e712725bc36d9; _ga=GA1.1.296539765.1686998466; __uuid=1686998466329.74; __tlog=1686998466337.60%7C00000000%7C00000000%7C00000000%7C00000000; acw_tc=ac11000116869984669203118e00cda4ac00996057bb86efd7b98636608823; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1686998467; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1686998583; _ga_54YTJKWN86=GS1.1.1686998465.1.1.1686998599.0.0.0; __session_seq=8; __uv_seq=8',
    'Origin': 'https://www.liepin.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.liepin.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=head_navigation&scene=init&workYearCode=0&ckId=sa96gv5zenc4rgokx7htzg10pk1ds118"}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '69bb5a87-42fd-41b2-91b9-93508e2c8c8e',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'ysT0K0X3RYidU-KYK3nk5Q',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'data': {
        'mainSearchPcConditionForm': {
            'city': '410',
            'dq': '410',
            'pubTime': '',
            'currentPage': 0,
            'pageSize': 40,
            'key': 'python',
            'suggestTag': '',
            'workYearCode': '0',
            'compId': '',
            'compName': '',
            'compTag': '',
            'industry': '',
            'salary': '',
            'jobKind': '',
            'compScale': '',
            'compKind': '',
            'compStage': '',
            'eduLevel': '',
            'otherCity': '',
        },
        'passThroughForm': {
            'ckId': 'gaq8t6xomq6oe26u1o14vais9s72m6b8',
            'scene': 'input',
            'skId': 'j3bssv9psz2ydz5l3fc2c6mq2uetl6d9',
            'fkId': 'j3bssv9psz2ydz5l3fc2c6mq2uetl6d9',
            'sfrom': 'search_job_pc',
        },
    },
}

response = requests.post(
    'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
print(response)